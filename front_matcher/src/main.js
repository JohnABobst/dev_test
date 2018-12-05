// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex';
import App from './App'
import router from './router'
import store from './store/store'
import axios from 'axios';

// import Router from 'vue-router'
import {
  Vuetify,
  VApp,
  VNavigationDrawer,
  VFooter,
  VMenu,
  VList,
  VSelect,
  VBtn,
  VCard,
  VDatepicker,
  VDataTable,
  VDivider,
  VDialog,
  VTabs,
  VForm,
  VPagination,
  VRadioGroup,
  VSwitch,
  VTextField,
  VCheckbox,
  VIcon,
  VGrid,
  VSubheader,
  VTextarea,
  VToolbar,
  VTooltip,
  transitions,
  VExpansionPanel,
  VDataIterator,
} from 'vuetify'
import '../node_modules/vuetify/src/stylus/app.styl'

Vue.use(Vuex);

Vue.use(Vuetify, {
  components: {
    VApp,
    VNavigationDrawer,
    VFooter,
    VMenu,
    VList,
    VSelect,
    VBtn,
    VCard,
    VDatepicker,
    VDataTable,
    VDivider,
    VDialog,
    VTabs,
    VForm,
    VPagination,
    VRadioGroup,
    VSwitch,
    VTextField,
    VCheckbox,
    VIcon,
    VGrid,
    VSubheader,
    VTextarea,
    VToolbar,
    VTooltip,
    transitions,
    VExpansionPanel,
    VDataIterator,
  },
  theme: {
    primary: '#00838F',
    secondary: '#703061',
    accent: '#8D6E63',
    error: '#C93926',
    info: '#9575CD',
    success: '#88A2AA',
    warning: '#462749'
  }
})

const config = {
  aria: true,
  classNames: {},
  classes: false,
  delay: 0,
  dictionary: null,
  errorBagName: 'errors', // change if property conflicts
  events: 'input|blur',
  fieldsBagName: 'fields',
  i18n: null, // the vue-i18n plugin instance
  i18nRootKey: 'validations', // the nested key under which the validation messsages will be located
  inject: true,
  locale: 'en',
  strict: true,
  validity: false,
};

Vue.config.productionTip = false

new Vue({
  el: '#app',
  store,
  router,
    data () {
    return {
      info: null
    }
  },
  components: { App },
  template: '<App/>'
})
