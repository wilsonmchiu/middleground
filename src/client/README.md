# client

### High level description of file structure

All your code should only be modifying the contents within client/src

```
├── src
│   ├── App.vue
│   ├── assets
│   │   ├── logo.png
│   │   └── logo.svg
│   ├── components
│   │   ├── Alert.vue
│   │   └── HelloWorld.vue
│   ├── main.js
│   ├── plugins
│   │   └── vuetify.js
│   ├── router.js
│   └── views
│       ├── Home.vue
│       ├── Login.vue
│       └── Register.vue
```

* __components/__ - are all User Interface elements or "vue components" are built.

* __main.js__ - Initializes App.vue and entry point for third party plugins

* __App.vue__ - Root component that is rendered first 

* __assets/__ - Any static images to be referenced 

* __plugins/__ - Initialize vue plugins in this folder

* __views/__ - Vue components that will act as pages in our website

### Add a component 

To make a componenet namded __foo__ you would make a foo.vue file in the src/components folder.

Components used in other components must be imported in the script section. 

Reference for structure of a vue component: https://vuejs.org/v2/guide/single-file-components.html

### To add a new "page" or endpoint

Steps to make a new page called with the url 'localhost:8080/boo' 

1) Make a new vue component in the __views/__ folder 
2) In __router.js__ :

```

...
import Boo from './views/Register.vue'
import Boo from './views/Boo.vue'

Vue.use(Router)

export default new Router({

	mode: 'history',
	base: process.env.BASE_URL, 
	routes:[
		{
			path: '/',
			name: 'home',
			component: Home
		},
    
		{
			path: '/register',
			name: 'register',
			component: Register
		},
		{
		        path: '/boo',
		        name: 'boo',
		        component: Boo
		 }

	]

})
```

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


