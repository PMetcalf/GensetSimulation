using System.Threading.Tasks;
using DatabaseController.Services;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace DatabaseController
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllers();

            services.AddSingleton<ICosmosDbService>(InitialiseCosmosClientInstanceAsync(
                Configuration.GetSection("CosmosDb")).GetAwaiter().GetResult());
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseHttpsRedirection();

            app.UseRouting();

            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });
        }

        /// <summary>
        /// Initialises Cosmos DB client connection and container.
        /// </summary>
        /// <param name="configurationSection"></param>
        /// <returns></returns>
        private static async Task<CosmosDBService> InitialiseCosmosClientInstanceAsync(IConfigurationSection configurationSection)
        {
            // Set connection parameters
            string databaseName = configurationSection.GetSection("DatabaseName").Value;
            string containerName = configurationSection.GetSection("ContainerName").Value;
            string account = configurationSection.GetSection("Account").Value;
            string key = configurationSection.GetSection("Key").Value;

            // Build client and services
            Microsoft.Azure.Cosmos.Fluent.CosmosClientBuilder clientBuilder =
                new Microsoft.Azure.Cosmos.Fluent.CosmosClientBuilder(account, key);

            Microsoft.Azure.Cosmos.CosmosClient client =
                clientBuilder.WithConnectionModeDirect().Build();

            CosmosDBService dBService = new CosmosDBService(client, databaseName, containerName);

            // Initialise database, if required
            Microsoft.Azure.Cosmos.DatabaseResponse database = await client.CreateDatabaseIfNotExistsAsync(databaseName);

            // Build the database container
            await database.Database.CreateContainerIfNotExistsAsync(containerName, "/id");

            return dBService;
        }
    }
}
