<template>
  <v-container>
  <v-app>

    

    <v-card
    color="grey lighten-4"
    flat
    height="200px"
    tile
  >
    <v-toolbar dense>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Taitoru</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>
  </v-card>
   

    


      <v-img
        height="100%"
        src="https://funart.pro/uploads/posts/2020-04/1587109612_41-p-chernie-foni-so-zvezdami-119.jpg"
      >
        <v-row
          align="end"
          class="fill-height"
        >
          <v-col
            align-self="start"
            class="pa-0"
            cols="12"
          >
            <v-avatar
              class="profile"
              color="blue"
              size="164"
              rounded="1"
            >
              <v-img src="https://cdn.donmai.us/original/de/72/__hoshimachi_suisei_hololive_drawn_by_hinata_kokage__de7265a8b8e37c286d867a946c6e47c4.png"></v-img>
            </v-avatar>
          </v-col>
          <v-col class="py-0">
            <v-list-item
              color="rgba(0, 0, 0, .4)"
              dark
            >
              <v-list-item-content>

                  <v-textarea
      background-color="light-blue"
      color="black"
      label="Another post emul2 "
    ></v-textarea>

    <v-textarea
      background-color="grey lighten-2"
      color="cyan"
      label="Another post Emulation"
    ></v-textarea>

    <v-textarea
      background-color="amber lighten-4"
      color="orange orange-darken-4"
      label="post emullation"
    ></v-textarea>

                <v-list-item-title class="text-h6">
                  suisyan
                </v-list-item-title>
                <v-list-item-subtitle>Waifu</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-col>
        </v-row>
      </v-img>
   </v-app>
<div id="app"></div>


      
  </v-container>
</template>

<script>
  export default {
    name: 'HelloWorld',

    data: () => ({
         rules: [v => v.length <= 25 || 'Max 25 characters'],
      value: 'Hello!',

    })
  }
</script>


