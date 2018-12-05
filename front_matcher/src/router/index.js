import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/HelloWorld'
import Matcher from '@/components/matcher/Matcher'
import Results from '@/components/matcher/Results'
import Upload from '@/components/recordings/Upload'
import Reports from '@/components/reports/Reports'
import ReportDetail from '@/components/reports/ReportDetail'
import store from '../store/store'
Vue.use(Router)

const routes = [
    {path: '/', component:Home,
        children: [

            {path:'/home', redirect:'/', component:Home},
    ]},
    {path: '/matcher', component: Matcher},
    {path: '/reports', component:Reports},
    {
        path:'/report_details/:id',
        name: 'report_details',
        component: ReportDetail
    },
    { path: '/recordings', component: Upload},
    {
        path:'/results/:id',
        name: 'results',
        component: Results,
        
    }
]

export default new Router( {mode: 'history', routes});
