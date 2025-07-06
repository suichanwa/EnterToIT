local currently_hovered = {}

-- Initialize global bookmarks table if it doesn't exist
script.on_init(function()
  if not global.bookmarks then global.bookmarks = {} end
end)

-- When the crafting menu is opened, add the Bookmarks frame
script.on_event(defines.events.on_gui_opened, function(event)
  if event.gui_type == defines.gui_type.crafting then
    local player = game.players[event.player_index]
    local crafting_menu = player.opened
    
    -- Add Bookmarks frame to the right of the crafting grid
    local crafting_grid = crafting_menu.children[1] -- Adjust if the grid is not the first child
    local bookmarks_frame = crafting_menu.add{
      type = "frame",
      name = "bookmarks_frame",
      direction = "vertical",
      caption = "Bookmarks"
    }
    bookmarks_frame.style.width = 50
    bookmarks_frame.style.top_margin = 10
    bookmarks_frame.location = {
      x = crafting_grid.location.x + crafting_grid.style.width + 10,
      y = crafting_grid.location.y
    }
    
    -- Populate with existing bookmarks
    if not global.bookmarks[player.index] then global.bookmarks[player.index] = {} end
    for _, recipe in pairs(global.bookmarks[player.index]) do
      local slot = bookmarks_frame.add{
        type = "sprite-button",
        sprite = "item/" .. recipe,
        number = player.get_craftable_count(recipe),
        tooltip = recipe
      }
      slot.tags = {recipe = recipe}
    end
  end
end)

-- Track hovered crafting slot
script.on_event(defines.events.on_gui_hover, function(event)
  local player = game.players[event.player_index]
  local element = event.element
  if element.parent and element.parent == player.opened.children[1] and element.type == "sprite-button" then
    currently_hovered[player.index] = element
  end
end)

script.on_event(defines.events.on_gui_leave, function(event)
  local player = game.players[event.player_index]
  if currently_hovered[player.index] == event.element then
    currently_hovered[player.index] = nil
  end
end)

-- Add hovered recipe to bookmarks when "A" is pressed
script.on_event("add-to-bookmarks", function(event)
  local player = game.players[event.player_index]
  local hovered_slot = currently_hovered[player.index]
  if hovered_slot and hovered_slot.valid then
    local recipe = hovered_slot.tooltip -- Assuming tooltip holds the recipe name
    if recipe and not table.contains(global.bookmarks[player.index], recipe) then
      table.insert(global.bookmarks[player.index], recipe)
      local bookmarks_frame = player.opened.bookmarks_frame
      if bookmarks_frame then
        local slot = bookmarks_frame.add{
          type = "sprite-button",
          sprite = "item/" .. recipe,
          number = player.get_craftable_count(recipe),
          tooltip = recipe
        }
        slot.tags = {recipe = recipe}
      end
    end
  end
end)

-- Handle clicking on bookmarks (left-click to craft, right-click to remove)
script.on_event(defines.events.on_gui_click, function(event)
  local element = event.element
  local player = game.players[event.player_index]
  if element.tags and element.tags.recipe and element.parent.name == "bookmarks_frame" then
    if event.button == defines.mouse_button_type.left then
      player.begin_crafting{recipe = element.tags.recipe, count = 1}
    elseif event.button == defines.mouse_button_type.right then
      for i, recipe in ipairs(global.bookmarks[player.index]) do
        if recipe == element.tags.recipe then
          table.remove(global.bookmarks[player.index], i)
          element.destroy()
          break
        end
      end
    end
  end
end)

-- Helper function to check if a value exists in a table
function table.contains(table, value)
  for _, v in pairs(table) do
    if v == value then return true end
  end
  return false
end