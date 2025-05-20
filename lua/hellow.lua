--- okey so im trynga learn lua so later on ill play with opencomputers in minecraft so let's go throw soma basics and make an task that later on i could make in the game

--[[
   1. Variables
   2. Functions
   3. Tables
   4. Loops
   5. Conditionals
]]--
--[[
   Variables
   Variables are used to store data that can be used later in the program.
   In Lua, you can create a variable by simply assigning a value to it.
]]--
--[[
   In Lua, variables are dynamically typed, meaning you don't need to declare the type of the variable.
   You can assign any value to a variable without specifying its type.
]]--
--[[
   You can create a variable by simply assigning a value to it.
   For example:
]]--
local a = 10
local b = 20

--[[
   Functions
   Functions are blocks of code that can be reused throughout your program.
   You can define a function using the function keyword, followed by the function name and parameters.
]]--

local function moveitem(item1, item2)

   local array1 = {item1}
   local array2 = {item2}

   for i = 1, #array1 do
      --move the item from array1 to array2
      table.insert(array2, array1[i])
      table.remove(array1, i)
   end

   print("Item moved from " .. item1 .. " to " .. item2)
end

--[[
   In this example, we define a function called moveitem that takes two parameters: item1 and item2.
   The function moves the item from item1 to item2.
]]--

--moveitem(b, a)

local function convertIntTOseconds(number)
   local seconds = number * 60
   print("The number " .. number .. " in seconds is: " .. seconds)
   
end

convertIntTOseconds(5)