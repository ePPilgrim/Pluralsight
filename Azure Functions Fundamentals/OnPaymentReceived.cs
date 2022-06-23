using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;

namespace Azure_Functions_Fundamentals
{
    public static class OnPaymentReceived
    {
        [FunctionName("OnPaymentReceived")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Function, "post", Route = null)] HttpRequest req,
            [Queue("orders")] IAsyncCollector<Order> orderQueue,
            [Table("orders")] IAsyncCollector<Order> orderTable,
            ILogger log)
        {
            log.LogInformation("Received a payment.");

            string requestBody = await new StreamReader(req.Body).ReadToEndAsync();
            Order data = JsonConvert.DeserializeObject<Order>(requestBody);
            await orderQueue.AddAsync(data);

            data.PartitionKey = "order";
            data.RowKey = data.OrderId;
            await orderTable.AddAsync(data);

            log.LogInformation($"Order {data.OrderId} received from Email {data.Email} for product {data.ProductId}.");

            return new OkObjectResult("Thank you for your purchase.");
        }
    }

    public class Order{
        public string PartitionKey { get; set; }
        public string RowKey { get; set; }
        public string OrderId {get; set;}
        public string ProductId {get; set;}
        public string Email{ get; set;}
        public decimal Price {get; set;}
    }
}
