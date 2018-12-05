<template>
    <v-container grid-list-lg xs12 >
      <v-layout row wrap>
        <v-flex xs12>
            <v-card>
                <v-card-text class='text-xs-center headline font-weight-light'>
                    Add songs to the database by uploading a CSV file.
                </v-card-text>
            </v-card>
        </v-flex>
        </v-layout>
        <v-layout  justify-center >

                <v-btn color="info"
                      class="white--text"
                      @click="uploadFile()"
                      >
                      Select
                      <v-icon right dark>folder_open</v-icon>
                  </v-btn>
                  <input style="display:none" type="file" id="file" ref="file" class='uploadButton' v-on:change="handleFileUpload()"/>
                  <v-btn color="info"
                        class="white--text"
                        @click="submitFile()"
                        >
                        Upload
                        <v-icon right dark>cloud_upload</v-icon>
                    </v-btn>

        </v-layout>
        <v-layout row wrap>
            <v-flex v-for="recording in recordings" :key="recording.id" xs12 md4>
                <v-card color="deep-purple lighten-1" class="white--text elevation-24 fill-height">
                    <v-card-title primary-title>
                        <div>
                            <h4  v-if="recording.artist !== ''" class=" font-weight-light">{{recording.artist}}</h4>
                            <h4 v-else class=' black--text font-weight-black font-italic'>Field Missing</h4>
                            <h4 display-1 v-if="recording.title !== ''" class=" font-weight-light">{{recording.title}}</h4>
                            <h4 v-else class=' black--text font-weight-black font-italic'>Field Missing</h4>
                            <h4 v-if="recording.isrc !== ''" class="font-weight-light">{{recording.isrc}}</h4>
                            <h4 v-else class='black--text font-weight-black font-italic'>Field Missing</h4>
                            <h4  v-if="recording.duration !== ''" class="font-weight-light">{{recording.duration}}</h4>
                            <h4 v-else class='black--text font-weight-black font-italic'>Field Missing</h4>
                        </div>
                    </v-card-title>
                </v-card>
            </v-flex>
            <v-card>
            </v-card>
        </v-layout>
    </v-container>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h4 {
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
import router from '../../router'
import { createNamespacedHelpers } from 'vuex'
const { mapState, mapActions, mapGetters } = createNamespacedHelpers('recordings')
export default {

    data: () => {
        return {
            file: '',

        }
    },
    computed: {
        ...mapState({
            recordings: state => state.recordings
        })
    },
    methods: {

        handleFileUpload() {
            this.file = this.$refs.file.files[0]
        },

        submitFile(){
            let formData = new FormData();
            formData.append('songs', this.file)
            axios.post(this.$store.state.recordings.endpoints.upload, formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(response => {
                    this.$store.state.recordings.recordings = response.data
                })
                router.push('/home')
        },

            uploadFile() {
                document.getElementById("file").click();
        }
    }
}
</script>
