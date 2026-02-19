using System;
using System.Data.SqlClient;

string db = "$server=localhost;database=mydb;user=postgress;password=password;";

using var connection = new SqlConnection(db);
