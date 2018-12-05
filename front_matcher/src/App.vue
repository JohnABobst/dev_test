​​<template>
  <div id="app">
    <v-app
      dark
      id="inspire"
    >
      <v-navigation-drawer
        fixed
        clipped
        v-model="drawer"
        app
      >
        <v-list dense>
          <v-list-tile v-for="item in items" :key="item.text" :to="item.path">
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>
                {{ item.text }}
              </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>


          </v-list>

          </v-list-tile>





        </v-list>
      </v-navigation-drawer>
      <v-toolbar
        color="deep-purple lighten-1"
        dense
        fixed
        clipped-left
        app
      >
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>

        <v-toolbar-title class="mr-5 align-center" to="/home">
          <span class="title">Matcher</span>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-layout row align-center style="max-width: 650px">

        </v-layout>
      </v-toolbar>

      <v-content>
        <v-container fluid fill-height>
          <v-layout justify-center>
            <v-flex xs12 sm10>
              <router-view/>
              
            </v-flex>
          </v-layout>
        </v-container>
      </v-content>
    </v-app>
  </div>
</template>
<script>
  export default {
  data: () => ({
      drawer: true,
      items: [
        { icon: 'home', text: 'Home', path: '/home' },
        { icon: 'bar_chart', text: 'Reports', path: '/reports' },
        { icon: 'audiotrack', text: 'Recordings', path: '/recordings' },

      ],

    }),
    props: {
      source: String
    },
     methods: {
        goBack () {
          window.history.length > 1
            ? this.$router.go(-1)
            : this.$router.push('/')
        },


    }
  }



</script>

        login () {
            this.$router.push({path: '/login'})
        }
    }
  }
</script>
