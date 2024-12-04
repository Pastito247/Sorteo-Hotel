import { createRouter, createWebHistory } from 'vue-router';
import Register from '../views/Register.vue';
import VerifyEmail from '../views/VerifyEmail.vue';
import Login from '../views/Login.vue';
import ChooseWinner from '../views/ChooseWinner.vue';
import ChangePassword from '../views/ChangePassword.vue';

const routes = [
  { path: '/', name: 'Register', component: Register },
  { path: '/change-password', name: 'ChangePassword', component: ChangePassword },
  { path: '/verify-email/:uidb64/:token/', name: 'VerifyEmail', component: VerifyEmail }, // Ajuste aquí
  { path: '/login', name: 'Login', component: Login },
  { 
    path: '/choose-winner', 
    name: 'ChooseWinner', 
    component: ChooseWinner,
    beforeEnter: (to, from, next) => {
      if (localStorage.getItem('access_token')) {
        next();
      } else {
        next('/login');
      }
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
