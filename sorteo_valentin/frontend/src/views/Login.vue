<template>
  <div class="login-container">
    <div class="form-container">
      <h1 class="title">Iniciar Sesión</h1>
      <form @submit.prevent="loginUser">
        <div class="input-group">
          <label for="email">Correo Electrónico</label>
          <input v-model="email" type="email" id="email" required />
        </div>
        <div class="input-group">
          <label for="password">Contraseña</label>
          <input v-model="password" type="password" id="password" required />
        </div>
        <button type="submit" class="btn submit-btn">Iniciar sesión</button>
      </form>
      <p v-if="error" class="error-message">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      error: ''
    };
  },
  methods: {
    async loginUser() {
      try {
        // Realiza la solicitud POST con las credenciales
        const response = await axios.post('http://127.0.0.1:8000/api/users/login/', {
          email: this.email,
          password: this.password
        });

        // Guarda el token de acceso en el almacenamiento local
        localStorage.setItem('access_token', response.data.access_token);

        // Redirige al usuario a la página de elegir ganador
        this.$router.push('/choose-winner');
      } catch (error) {
        // Si ocurre un error, muestra el mensaje
        this.error = error.response?.data?.error || 'Credenciales inválidas';
      }
    }
  }
};
</script>

<style scoped>
.login-container {
  height: 100vh;
  background-image: url('../assets/img/login.jpg');
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.form-container {
  background-color: rgba(255, 255, 255, 0.9);
  padding: 2rem;
  border-radius: 10px;
  max-width: 400px;
  width: 100%;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.title {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  color: #333;
}

.input-group {
  margin-bottom: 1rem;
  text-align: left;
}

label {
  display: block;
  font-size: 1rem;
  margin-bottom: 0.5rem;
  color: #333;
}

input {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  margin-bottom: 1rem;
}

.submit-btn {
  padding: 1rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s;
  width: 100%;
}

.submit-btn:hover {
  background-color: #45a049;
}

.error-message {
  margin-top: 1rem;
  color: red;
  font-size: 1rem;
}
</style>
