using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using SimulationWebservice.Services;

namespace SimulationWebservice
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
                Configuration.GetSection("CosmosDB")).GetAwaiter().GetResult());
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
        /// Create a Cosmos DB and a container with the specified partition key.
        /// </summary>
        /// <returns></returns>
        private static async Task<CosmosDBService> InitialiseCosmosClientInstanceAsync(IConfigurationSection configurationSection)
        {
            // Retrieve DB and container parameters.
            string databaseName = configurationSection.GetSection("DatabaseName").Value;
            string containerName = configurationSection.GetSection("ContainerName").Value;
            string account = configurationSection.GetSection("Account").Value;
            string key = configurationSection.GetSection("Key").Value;

            // Build the client and services.
            Microsoft.Azure.Cosmos.Fluent.CosmosClientBuilder clientBuilder =
                new Microsoft.Azure.Cosmos.Fluent.CosmosClientBuilder(account, key);

            Microsoft.Azure.Cosmos.CosmosClient client =
                clientBuilder.WithConnectionModeDirect().Build();

            CosmosDBService dBService = new CosmosDBService(client, databaseName, containerName);

            // Prepare the database.
            Microsoft.Azure.Cosmos.DatabaseResponse database = await client.CreateDatabaseIfNotExistsAsync(databaseName);

            // Prepare the container.
            await database.Database.CreateContainerIfNotExistsAsync(containerName, "/id");

            return dBService;
        }
    }
}
