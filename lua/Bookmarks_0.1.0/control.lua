local currently_selected_recipe = {}
local bookmarks_frame_open       = {}

script.on_init(function()
  global.bookmarks = {}
end)

script.on_load(function()
  -- global.bookmarks already exists after load
end)

-- When the player inventory is opened, show the Bookmarks frame
script.on_event(defines.events.on_gui_opened, function(event)
  if event.gui_type ~= defines.gui_type.entity then return end
  local player = game.players[event.player_index]
  if event.entity ~= player.character then return end

  bookmarks_frame_open[player.index] = true
  if player.gui.screen.bookmarks_frame then
    player.gui.screen.bookmarks_frame.destroy()
  end

  local frame = player.gui.screen.add{
    type      = "frame",
    name      = "bookmarks_frame",
    direction = "vertical",
    caption   = "Bookmarks"
  }
  frame.style.minimal_width   = 200
  frame.style.maximal_height  = 400
  frame.location              = {400, 100}

  frame.add{
    type    = "label",
    caption = "Start crafting a recipe, then press Ctrl+A to bookmark it"
  }.style.font = "default-small"

  local pane = frame.add{ type = "scroll-pane", name = "bookmarks_scroll" }
  pane.style.minimal_height = 100
  pane.add{ type = "flow", name = "bookmarks_flow", direction = "vertical" }

  local list = global.bookmarks[player.index] or {}
  for _, r in ipairs(list) do
    if player.force.recipes[r] and player.force.recipes[r].enabled then
      local btn = pane.bookmarks_flow.add{
        type    = "sprite-button",
        name    = "bookmark_" .. r,
        sprite  = "recipe/" .. r,
        tooltip = player.force.recipes[r].localised_name
      }
      btn.tags = { recipe = r }
      btn.style.size = 40
    end
  end
end)

-- Destroy the frame when inventory closes
script.on_event(defines.events.on_gui_closed, function(event)
  if event.gui_type ~= defines.gui_type.entity then return end
  local player = game.players[event.player_index]
  if event.entity ~= player.character then return end

  bookmarks_frame_open[player.index] = false
  if player.gui.screen.bookmarks_frame then
    player.gui.screen.bookmarks_frame.destroy()
  end
end)

-- Track the last recipe queued for crafting
script.on_event(defines.events.on_player_crafting_queued, function(event)
  local player      = game.players[event.player_index]
  local recipe_name = event.recipe.name
  currently_selected_recipe[player.index] = recipe_name
  player.print("Crafting queued: " .. recipe_name .. " (Ctrl+A to bookmark)")
end)

-- Handle clicks on bookmark buttons (left = craft, right = remove)
script.on_event(defines.events.on_gui_click, function(event)
  local el     = event.element
  local player = game.players[event.player_index]
  if not (el.tags and el.tags.recipe) then return end

  local r = el.tags.recipe
  if event.button == defines.mouse_button_type.left then
    if player.force.recipes[r] and player.force.recipes[r].enabled then
      player.begin_crafting{ recipe = r, count = 1 }
      player.print("Crafting " .. r)
    end
  elseif event.button == defines.mouse_button_type.right then
    local list = global.bookmarks[player.index]
    if list then
      for i, v in ipairs(list) do
        if v == r then
          table.remove(list, i)
          el.destroy()
          player.print("Removed " .. r .. " from bookmarks")
          break
        end
      end
    end
  end
end)

-- Handle the custom-input Ctrl+A to add a bookmark
script.on_event("add-to-bookmarks", function(event)
  local player = game.players[event.player_index]
  if not bookmarks_frame_open[player.index] then
    player.print("Open your inventory first.")
    return
  end

  local r = currently_selected_recipe[player.index]
  if not r and player.crafting_queue_size > 0 then
    r = player.crafting_queue[1].recipe
    player.print("Using queue recipe: " .. r)
  end
  if not r then
    player.print("No recipe to bookmark.")
    return
  end

  global.bookmarks[player.index] = global.bookmarks[player.index] or {}
  local list = global.bookmarks[player.index]
  for _, v in ipairs(list) do
    if v == r then
      player.print(r .. " already bookmarked.")
      return
    end
  end

  table.insert(list, r)
  local frame = player.gui.screen.bookmarks_frame
  if frame and frame.bookmarks_scroll then
    local flow = frame.bookmarks_scroll.bookmarks_flow
    local btn = flow.add{
      type    = "sprite-button",
      name    = "bookmark_" .. r,
      sprite  = "recipe/" .. r,
      tooltip = player.force.recipes[r].localised_name
    }
    btn.tags       = { recipe = r }
    btn.style.size = 40
  end
  player.print("Bookmarked " .. r)
end)