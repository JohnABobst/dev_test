import axios from 'axios';
import router from '../../router'



const state = {

        recordings: [],
        endpoints: {
            recordings: 'http://127.0.0.1:8000/recordings',
            upload: 'http://127.0.0.1:8000/upload'
        }
}
mounted: {

    axios.get(state.endpoints.recordings)
    .then(response =>(state.recordings = response.data));



}
const mutations = {}

const getters = {}

const actions = {}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
