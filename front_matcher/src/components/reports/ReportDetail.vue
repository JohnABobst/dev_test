<template>
  <v-container fluid grid-list-lg pa-1>
      <v-layout row wrap >
        <v-flex  xs12 >
                <v-card  color="deep-purple darken-2" class="white--text tile elevation-24">
                  <v-card-title  primary-title >
                      <v-card-text class='text-xs-center headline font-weight-light'>
                          Match Report {{selected_report.id}}
                    </v-card-text>
                  </v-card-title>
              </v-card>
        </v-flex>
      </v-layout>
    <v-layout v-for='result in input_songs' row wrap :key='result.id'>
        <v-flex  xs12 sm6 >
            <v-card color="deep-purple lighten-1" class="white--text elevation-24 fill-height">
                <v-card-title primary-title>
                    <v-flex>
                        <h4  v-if="result.artist !== ''" class=" font-weight-light">{{result.artist}}</h4>
                        <h4 v-else class=' black--text font-weight-black font-italic'>Artist: Field Missing</h4>
                        <h4 display-1 v-if="result.title !== ''" class=" font-weight-light">{{result.title}}</h4>
                        <h4 v-else class=' black--text font-weight-black font-italic'>Title: Field Missing</h4>
                        <h4 v-if="result.isrc !== ''" class="font-weight-light">{{result.isrc}}</h4>
                        <h4 v-else class='black--text font-weight-black font-italic'>ISRC Field Missing</h4>
                        <h4  v-if="result.duration !== ''" class="font-weight-light">{{result.duration}}</h4>
                        <h4 v-else class='black--text font-weight-black font-italic'>Duration Field Missing</h4>
                    </v-flex>
                </v-card-title>
            </v-card>
        </v-flex>
        <v-flex sm6 xs12 d-flex  >
                <v-card  width="270px" color="default"  class="white--text tile fill-height" >
                         <v-card-title  primary-title >
                             <v-flex v-if="result.match !== null" >
                                 <h5 v-if="result.match.artist !== ''" class=" font-weight-light" >{{result.match.artist}}</h5>
                                 <h5 v-else class='black--text font-weight-black font-italic'>Field Missing</h5>
                                 <h5  v-if="result.match.title !== ''" class=" font-weight-light">{{result.match.title}}</h5>
                                 <h5 v-else  class='black--text font-weight-black font-italic'>Field Missing</h5>
                                 <h5 v-if="result.match.isrc !== ''" class=" font-weight-light">{{result.match.isrc}}</card-text></h5>
                                 <h5 v-else class='black--text font-weight-black font-italic'>Field Missing</h5>
                                 <h5  v-if="result.match.duration !== ''" class=" font-weight-light"> {{result.match.duration}}</h5>
                                 <h5 v-else class='black--text font-weight-black font-italic'>Field Missing</h5>
                             </v-flex>
                             <v-flex v-else color='warning' >
                                 <h4 >
                                     There are no matches in the database
                                 </h4>
                             </v-flex>
                         </v-card-title>
                     </v-card>
                </v-flex>
    </v-layout>
  </v-container>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h1, h5 {
  font-weight: thin;

}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

<script>

import axios from 'axios';
import router from '../../router'
import { createNamespacedHelpers } from 'vuex'
const { mapState, mapActions, mapGetters } = createNamespacedHelpers('matcher')

export default {
    computed:{
        ...mapState({
            input_songs: state => state.selected_report.input_songs,
            selected_report: state => state.selected_report
        })
},

}






</script>
