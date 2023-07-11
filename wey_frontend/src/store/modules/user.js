import mutations from "@/store/mutations"
import axios from "axios"

const {
    INIT_STORE,
    SET_TOKEN,
    REMOVE_TOKEN,
    SET_USER_INFO,
    REFRESH_TOKEN,
} = mutations

const userStore = {
    namespaced: true,
    state: {
        user: {
            isAuthenticated: false,
            id: null,
            name: null,
            email: null,
            access: null,
            refresh: null,
            avatar: null
        }
    },
    getters: {
        getIsAuthenticated: ({ user }) => user.isAuthenticated,
        getId: ({ user }) => user.id,
        getName: ({ user }) => user.name,
        getEmail: ({ user }) => user.email,
        getAccess: ({ user }) => user.access,
        getRefresh: ({ user }) => user.refresh,
        getAvatar: ({ user }) => user.avatar,
    },
    mutations: {
        [INIT_STORE](state) {
            state.user.access = localStorage.getItem('user.access')
            state.user.refresh = localStorage.getItem('user.refresh')
            state.user.id = localStorage.getItem('user.id')
            state.user.name = localStorage.getItem('user.name')
            state.user.email = localStorage.getItem('user.email')
            state.user.avatar = localStorage.getItem('user.avatar')
            state.user.isAuthenticated = true
        },
        [SET_TOKEN](state, data) {
            state.user.access = data.access
            state.user.refresh = data.refresh
            state.user.isAuthenticated = true
        },
        [REMOVE_TOKEN](state) {
            state.user.refresh = null
            state.user.access = null
            state.user.isAuthenticated = false
            state.user.id = null
            state.user.name = null
            state.user.email = null
            state.user.avatar = null
        },
        [SET_USER_INFO](state, user) {
            state.user.id = user.id
            state.user.name = user.name
            state.user.email = user.email
            state.user.avatar = user.avatar
        },
        [REFRESH_TOKEN](state, token){
            state.user.access = token
        },
    },
    actions: {
        initStore({ commit, dispatch, state }) {
            console.log('initStore', localStorage.getItem('user.access'))

            if (localStorage.getItem('user.access')) {
                console.log('User has access!')

                commit(INIT_STORE)
                dispatch('refreshToken')

                console.log('Initialized user:', state.user)
            }
        },

        setToken({ commit }, data) {
            console.log('setToken', data)

            commit(SET_TOKEN, data)

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)

            console.log('user.access: ', localStorage.getItem('user.access'))
        },

        removeToken({ commit }) {
            console.log('removeToken')

            commit(REMOVE_TOKEN)

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.avatar', '')
        },

        setUserInfo({ commit, state }, user) {
            console.log('setUserInfo', user)

            commit(SET_USER_INFO, user)

            localStorage.setItem('user.id', state.user.id)
            localStorage.setItem('user.name', state.user.name)
            localStorage.setItem('user.email', state.user.email)
            localStorage.setItem('user.avatar', state.user.avatar)

            console.log('User', state.user)
        },

        refreshToken({ commit, state, dispatch }) {
            axios.post('/api/refresh/', {
                refresh: state.user.refresh
            })
                .then(response => {
                    commit(REFRESH_TOKEN, response.data.access)

                    localStorage.setItem('user.access', response.data.access)

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch(error => {
                    console.log(error)
                    dispatch('removeToken')
                })
        },
    }
}

export default userStore
