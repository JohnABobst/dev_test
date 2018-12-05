import axios from 'axios';
import router from '../../router'



const state = {
        reports: [],
        selected_report: {
            input_songs: [

            ]
        },
        endpoints: {
            select_match: 'http://127.0.0.1:8000/select_match',
            matcher: 'http://127.0.0.1:8000/matcher',
            add_song: 'http://127.0.0.1:8000/add_song'
        },
        created_response: {

            input_songs: [],
            match_choices: [
                {

                        song: {
                            artist: '',
                            title:''
                        },
                        possible_matches: [
                            {
                                artist: '',
                                title:''
                            }
                        ]
                    }

        ],
        file: '',
    }
}

mounted: {
    axios.get(state.endpoints.matcher)
    .then(response =>(state.reports = response.data));
}

const mutations = {

        post_song(state, index) {
            state.created_response.match_choices.splice(index,1)
        },

        select_matches(state, id){
            state.selected_report = state.reports.find(report => {
                return report.id === id
            });
            router.push({name:'matches',
                params: {id: state.selected_report.id}
            })
        },
        remove_from_list(state, index){
            state.created_response.match_choices.splice(index,1)
        },
        set_report(state, id) {
            state.selected_report = state.reports.find(report => {
                 return report.id === id
            })
            router.push({name:'report_details', params: {
                id: id
            }})
        }
}

const getters = {}

const actions = {

        matches({commit},id) {
            commit('get_report', id)
        },
        no_selection({commit}, index) {
            commit('remove_from_list', index)
        },
        submit_file({commit}){
            commit('post_file')
        },
        report_details({commit}, id) {
            commit('set_report', id)
        }
    }

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
