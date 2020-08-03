using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using BMRSDataWebService.Services;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.HttpsPolicy;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace BMRSDataWebService
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
            string databaseName;
            string containerName;
            string account;
            string key;

            // Build client and services
            Microsoft.Azure.Cosmos.Fluent.CosmosClientBuilder clientBuilder =
                new Microsoft.Azure.Cosmos.Fluent.CosmosClientBuilder(account, key); 

            // Initialise database, if required

            // Build the database container
        }
    }
}
