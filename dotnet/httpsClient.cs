using System.Net.Http;
using System.Text.Json;

HttpClient client = new HttpClient();
HttpResponseMessage response = await client.GetAsync("https://jsonplaceholder.typicode.com/todos");
string content = await response.Content.ReadAsStringAsync();
await File.WriteAllTextAsync("todos.json", content);
