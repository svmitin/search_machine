import api from '@/api/RepositoryFactory.js'
import router from '@/router'

const state = () => ({
    is_authorized: false,
    search_text: 'IKEA Омск',
    search_response: {}
})

const getters = {
    isAuthorized: (state) => {
        return state.is_authorized
    }
}

const actions = {
    // Действия. Асинхронны. Чтобы изменить состояние (state) вызывают мутацию
    GET_QUERY_RESPONSE: async (context, name) => {
        let {data} = await Axios.post('http://api.freedom:8000/search?query=' + this.search_text);

        if (data.status == 200) {
            context.commit('SET_QUERY_RESPONSE', name);
        }
    },
}

const mutations = {
    // Мутации/Сеттеры. Синхронны
    // ВОЗЬМИТЕ ЗА ПРАКТИКУ НИКОГДА НЕ ИНИЦИИРОВАТЬ МУТАЦИИ НАПРЯМУЮ. ДЛЯ ЭТОГО ВСЕГДА ИСПОЛЬЗУЙТЕ ДЕЙСТВИЯ
    SET_SEARCH_TEXT(state, payload) {
        state.search_text = payload
    },
    SET_QUERY_RESPONSE(state, payload) {
        state.search_response = payload
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}
