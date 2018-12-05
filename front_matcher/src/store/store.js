// store.js
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import matcher from './modules/matcher'
import recordings from './modules/recordings'


Vue.use(Vuex)
export default new Vuex.Store({

    modules: {

        recordings,
        matcher
    },
state: {},

getters: {}
})
