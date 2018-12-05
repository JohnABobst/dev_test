<template>
  <v-container fluid grid-list-lg pa-1>
      <v-layout row wrap >
          <v-flex xs3 v-for="report in reports" :key='report.id'>
              <v-card>
                  <v-card-text>
                      <h3>Report ID: {{report.id}}</h3>
                  </v-card-text>
                  <v-card-actions>
                      <v-btn small color='info'@click="report_details(report.id)">View Details</v-btn>
                  </v-card-actions>
              </v-card>
          </v-flex>
        </v-layout>
  </v-container>
</template>

<style scoped>
</style>
<script>

import axios from 'axios';
import router from '../../router'
import { createNamespacedHelpers } from 'vuex'
const { mapState, mapActions, mapGetters } = createNamespacedHelpers('matcher')

export default {

    computed:{
        ...mapState({
            reports: state => state.reports
        })

    },

    methods: {
        ...mapActions([
        'report_details',
        'matches'
        ])
    }
}
</script>
