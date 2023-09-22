<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="main-left">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-2xl">Log in</h1>

        <p class="mb-6 text-gray-500">
          Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
          Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
        </p>

        <p class="font-bold">
          Don't have an account? <RouterLink :to="{'name': 'signup'}" class="underline">Click here</RouterLink> to create one!
        </p>
      </div>
    </div>

    <div class="main-right">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-6" v-on:submit.prevent="submitForm">
          <div>
            <label>E-mail</label><br>
            <input type="email" v-model="form.email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
          </div>

          <div>
            <label>Password</label><br>
            <input type="password" v-model="form.password" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
          </div>

          <template v-if="errors.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-6">
              <p v-for="error in errors" :key="error">
                {{ error }}
              </p>
            </div>
          </template>

          <div>
            <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Log in</button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <Toast/>
</template>

<script>
import axios from "axios"
import {mapActions} from "vuex";
import Toast from '../components/Toast.vue'

export default {
  name: "Login",
  components: {
    Toast
  },
  data: () => ({
    form: {
      email: '',
      password: '',
    },
    errors: [],
  }),
  methods: {
    ...mapActions('toast', ['showToast', ]),
    ...mapActions('user', ['setToken', 'setUserInfo', ]),
    async submitForm() {
      this.errors = []

      if (this.form.email === '') {
        this.errors.push('Your email is missing')
      }

      if (this.form.password === '') {
        this.errors.push('Your password is missing')
      }

      if (this.errors.length === 0) {
        await axios.get('api/check_credentials/', {
          params: {
            email: this.form.email,
            password: this.form.password
          }
        })
            .then(response => {
              // console.log('response from check email', response.data)

              // response.data

              if (!response.data.email_exists) {
                this.errors.push("The specified email doesn't exist")
                console.log('email не существует')
              } else if (response.data.credentials_valid) {
                console.log('Всё хорошо, всё классно')
                axios.post('/api/login/', this.form)
                    .then(response => {
                      // console.log('response', response.data)
                      this.setToken(response.data)
                      axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                      let auth_user = {}
                      let myDct = response.data

                      for (const key in myDct) {
                        if (myDct.hasOwnProperty(key)) {
                          const value = myDct[key]
                          if (key !== 'access' && key !== 'refresh') {
                            auth_user[key] = value
                          }
                        }
                      }
                      // console.log('auth_user', auth_user)
                      this.setUserInfo(auth_user)
                      this.$router.push({ name: 'feed' })
                    })
                    .catch(error => {
                      console.log('Error ', error)
                      console.log('Mistake. Check the entered data')
                      this.showToast({
                        duration: 5000,
                        message: 'Mistake. Check the entered data',
                        style: 'bg-red-300'})
                    })
                    .finally(() => {
                      if (this.errors.length === 0) {
                        this.showToast({
                          duration: 5000,
                          message: 'Success login',
                          style: 'bg-emerald-500'})
                      }
                    })

              } else {
                this.errors.push('Incorect password')
                console.log('Неправильный пароль')
              }
            })
            .catch(error => {
              console.log('Error from check', error)
            })

        // await axios.post('/api/login/', this.form)
        //     .then(response => {
        //       // console.log('response', response.data)
        //       this.setToken(response.data)
        //       axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
        //       let auth_user = {}
        //       let myDct = response.data
        //
        //       for (const key in myDct) {
        //         if (myDct.hasOwnProperty(key)) {
        //           const value = myDct[key]
        //           if (key !== 'access' && key !== 'refresh') {
        //             auth_user[key] = value
        //           }
        //         }
        //       }
        //       // console.log('auth_user', auth_user)
        //       this.setUserInfo(auth_user)
        //       this.$router.push({ name: 'feed' })
        //     })
        //     .catch(error => {
        //       console.log('Error ', error)
        //       console.log('Mistake. Check the entered data')
        //       this.showToast({
        //         duration: 5000,
        //         message: 'Mistake. Check the entered data',
        //         style: 'bg-red-300'})
        //     })
        //     .finally(() => {
        //       if (this.errors.length === 0) {
        //         this.showToast({
        //           duration: 5000,
        //           message: 'Success login',
        //           style: 'bg-emerald-500'})
        //       }
        //     })
      }



    },
  },
}
</script>

<style scoped>

</style>