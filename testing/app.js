const app = Vue.createApp({
    //data, function, templates
    //template:'<h2>I am something</h2>'
    
    data(){
        return{
            title:'Pikachu',
            type:'Electric',
            number:1,
            log_counter: true,
        }
    },
    
    methods: {
        changeTitle(title){
            console.log("change name to charmander")
            this.title = title
        },
        HandleEventMO(){
            counter++
            console.log("mouseover")
            if(counter % 2 == 0)
                this.title = 'pikachu'
            else
                this.title = 'pikapikapikachu'
                
        },
        HandleEventDC(){
            if(this.log_counter==true){
                this.log_counter = false
                this.type = 'water'
            }
            else{
                this.log_counter = true
                this.type = 'electric'
            }

                
        }
        
    }
})
counter = 1

app.mount('#app_1')