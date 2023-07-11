import { createStore } from 'vuex'
import toast from "./modules/toast";
import user from "./modules/user";

const store = createStore({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    toast,
    user,
  }
})

export default store
