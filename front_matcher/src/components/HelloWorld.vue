<template>
    <v-container grid-list-lg xs12 >
        <v-layout row wrap>
            <v-flex xs12>
                <v-card>
                  <v-card-text>
                    <h3 class="display-3 text-xs-center">Weclome to Matcher</h3>
                  </v-card-text>
              </v-card>
          </v-flex>
      </v-layout>
      <v-layout row wrap>
        <v-flex xs12>
            <v-card>
                <v-card-text class='text-xs-center font-weight-light'>
                    <h2>To begin upload a CSV file.</h2>
                </v-card-text>
            </v-card>
        </v-flex>
        </v-layout>
        
        <v-layout  justify-center row wrap>
                <v-btn color="info"
                      class="white--text"
                      @click="uploadFile()"
                      >
                      Select
                      <v-icon right dark>folder_open</v-icon>
                  </v-btn>
                  <input style="display:none" type="file" id="file" ref="file" class='uploadButton' v-on:change="mount_file()"/>
                  <v-btn color="info"
                        class="white--text"
                        @click="submit_file()"
                        >
                        Upload
                        <v-icon right dark>cloud_upload</v-icon>
                    </v-btn>
                </v-layout>
    </v-container>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: thin;

}
.uploadButton {
    border-radius:6px;
    background-color: #9575CD;
    color: #D1C4E9;
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
import router from '../router'

import nextTick from 'vue'

export default {

    data() {
        return {
            file: ''
        }
    },

methods: {

    uploadFile() {
        document.getElementById("file").click();
    },

    mount_file() {
        this.file = this.$refs.file.files[0]

    },

    submit_file(){
        let form_data = new FormData();
        form_data.append('songs', this.file);
        axios.post(this.$store.state.matcher.endpoints.matcher, form_data, {
            header: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(response => this.$store.state.matcher.created_response=response.data);
        this.$nextTick(function() {
            router.push({path: '/matcher'})
        })
    }



}
}
</script>
