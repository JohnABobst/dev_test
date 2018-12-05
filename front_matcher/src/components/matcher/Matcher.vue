<template>
  <v-container fluid grid-list-lg pa-1>

          <v-expansion-panel class='taller'>

              <v-expansion-panel-content v-for='(input, index) in match_report' :key='input.id'>

                <div  slot="header">
                    {{input.song.title}}
                </div>
                <v-layout row wrap>
                    <v-flex  xs12 md12 lg3 >
                        <v-card color="deep-purple lighten-1" class="white--text elevation-24 fill-height">

                                <v-flex>


                                    <h4 v-if="input.song.artist !== ''" class=" font-weight-light">{{input.song.artist}}</h4>
                                    <h4 v-else class=' black--text font-weight-black font-italic'>Field Missing</h4>
                                    <h4 display-1 v-if="input.song.title !== ''" class=" font-weight-light">{{input.song.title}}</h4>
                                    <h4 v-else class=' black--text font-weight-black font-italic'>Field Missing</h4>
                                    <h4 v-if="input.song.isrc !== ''" class="font-weight-light">{{input.song.isrc}}</h4>
                                    <h4 v-else class='black--text font-weight-black font-italic'>Field Missing</h4>
                                    <h4  v-if="input.song.duration !== ''" class="font-weight-light">{{input.song.duration}}</h4>
                                    <h4 v-else class='black--text font-weight-black font-italic'>Field Missing</h4>
                                </v-flex>

                            <v-card-actions>
                                <v-btn small color='blue-grey darken-3' v-on:click='no_selection(index)'>Select None</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-flex>

                    <v-flex md12 xs12 lg3 d-flex v-for='(match) in input.possible_matches' :key="match.id" >
                            <v-card  color="default"  class="white--text tile" >


                                         <v-flex v-if="match.match_percentage !== 'There are no matches in the database'" >

                                             <h5 v-if="match.artist !== ''" class=" font-weight-light" >{{match.artist}}</h5>
                                             <h5 v-else class='red--text'>Field Missing</h5>
                                             <h5  v-if="match.title !== ''" class=" font-weight-light">{{match.title}}</h5>
                                             <h5 v-else  class='red--text'>Field Missing</h5>
                                             <h5 v-if="match.isrc !== ''" class=" font-weight-light">{{match.isrc}}</card-text></h5>
                                             <h5 v-else class='red--text font-weight-light'>Field Missing</h5>
                                             <h5  v-if="match.duration !== ''" class=" font-weight-light"> {{match.duration}}</h5>
                                             <h5 v-else class='red--text font-weight-light'>Field Missing</h5>
                                             <h5 class=" font-weight-light" >{{match.match_percentage}}% Match</h5>
                                         </v-flex>
                                         <v-flex v-else color='warning' >
                                             <h5 class=' font-weight-light'>
                                                 There are no matches in the database
                                             </h5>
                                         </v-flex>

                                     <v-card-actions >                                         
                                         <v-btn v-if="match.match_percentage !== 'There are no matches in the database'" small color="info" v-on:click='select_match(input.song.id, match.id, index)'>Select Match</v-btn>
                                         <v-btn  v-else small color="deep-purple darken-2"v-on:click="add_song(index, input.song)">Add Song</v-btn>
                                    </v-card-actions>

                                 </v-card>

                            </v-flex>

                </v-layout>


              </v-expansion-panel-content>


      </v-expansion-panel>

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
            match_report: state => state.created_response.match_choices
        }),
    },
    methods: {
        ...mapActions([

            'no_selection'

        ]),
        add_song(index, match) {
            axios.post(this.$store.state.matcher.endpoints.add_song, match).then(response => {
                this.$store.state.recordings.recordings.push(response.data)
                this.$store.state.matcher.created_response.match_choices.splice(index,1)
            })


        },
        select_match(input_recording_id, match_id,index) {
        axios.post(this.$store.state.matcher.endpoints.select_match +'/' +input_recording_id+'/'+match_id)
            .then(this.$store.state.matcher.created_response.match_choices.splice(index,1))
        if (this.$store.state.matcher.created_response.match_choices.length === 0) {
            axios.get(this.$store.state.matcher.endpoints.matcher + '?id=' + this.$store.state.matcher.created_response.id)
                .then(response => {
                    this.$store.state.matcher.selected_report = response.data;
                    router.push({name:'results',params: {id:this.$store.state.matcher.created_response.id}
                })
                axios.get(this.$store.state.matcher.endpoints.matcher).then(response => {
                    this.$store.state.matcher.reports = response.data;

                })

            })


            }
        },
    }
}
</script>
