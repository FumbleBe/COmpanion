<template>
    <div>
        <h2>Login</h2>
        <input type="text" v-model="username" placeholder="Username">
        <input type="password" v-model="password" placeholder="Password">
        <button @click="login">Login</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            password: ''
        };
    },
    methods: {
        async login() {
            try {
                const response = await fetch('http://companion.lambsofgod.be:8000/api/token/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        username: this.username,
                        password: this.password
                    })
                });
                const data = await response.json();
                const token = data.access;
                console.log(token); // JWT token
            } catch (error) {
                console.error('Error:', error);
            }
        }
    }
};
</script>
