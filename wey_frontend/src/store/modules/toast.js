import mutations from "@/store/mutations"

const {
    SHOW_TOAST,
    HIDE_TOAST,
    SET_SHOW_TOAST,
} = mutations

const toastStore = {
    namespaced: true,
    state: {
        ms: 0,
        message: '',
        classes: '',
        isVisible: false
    },
    getters: {
        getMs: ({ ms }) => ms,
        getMessage: ({ message }) => message,
        getClasses: ({ classes }) => classes,
        getIsVisible: ({ isVisible }) => isVisible,
    },
    mutations: {
        [SET_SHOW_TOAST](state, payload) {
            state.ms = parseInt(payload.duration)
            // str => int
            state.message = payload.message
            state.classes = payload.style
            state.isVisible = true
            setTimeout(() => {
                state.classes += ' -translate-y-28'
            }, 10)
            setTimeout(() => {
                state.classes = state.classes.replace('-translate-y-28', '')
            }, state.ms - 500)
            setTimeout(() => {
                state.isVisible = false
            }, state.ms)
        },
    },
    actions: {
        showToast({ commit }, { duration, message, style }) {
            console.log('showToast')
            commit(SET_SHOW_TOAST, { duration, message, style })
        }
    }
}

export default toastStore
