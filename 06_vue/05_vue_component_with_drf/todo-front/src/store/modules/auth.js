import jwtDecode from 'jwt-decode'

const state = {
  token: null,
  loading: false,
}

// 데이터(state)를 변경하지 않음
// 데이터를 원본 그대로 또는 가공된 데이터를 사용
const getters = {
  isLoggedIn: function(state) {
    return state.token ? true : false
  },
  requestHeader: function(state) {
    return {
      headers: {
        Authorization: 'JWT ' + state.token
      }
    }
  },
  userId: function(state) {
    return state.token ? jwtDecode(state.token).user_id : null
  }
}

// 상태(token)를 받아 state 를 update
const mutations = {
  setToken: function(state, token) {
    state.token = token
  },
  setLoading: function(state, status) {
    state.loading = status
  }
}

// 비동기 logic(axios로 django 서버에 로그인/로그아웃 요청)
// options: action 에서 사용할 수 있도록 만든 객체
//   vuex 에서 제공하는, actions 함수에서 사용 가능한 option 이 들어있는 객체
const actions = {
  // commit 은 첫 번째 인자로 mutations 에 정의한 함수를 받음
  // 두 번째 인자로 token 을 받아 mutations 에 정의된 함수를 통해 state 변경
  login: function(options, token) {
    options.commit('setToken', token)
  },
  // 로그아웃의 경우 추가로 받는 인자는 없고, token 상태를 null 로 변경
  logout: function(options) {
    // token 상태 null
    options.commit('setToken')
  },
  startLoading: function(options) {
    options.commit('setLoading', true)
  },
  endLoading: function(options) {
    options.commit('setLoading', false)
  }
}

export default {
  state,
  getters,
  mutations,
  actions,
}
