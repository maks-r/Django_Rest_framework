import React from 'react'
import axios from 'axios'
import UserList from './components/UserList.js'
import ProjectList from './components/ProjectList.js'
import ToDoList from './components/ToDoList.js'
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation} from 'react-router-dom'
import LoginForm from './components/Loginform.js'


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': []
        }
    }

     obtainAuthToken(login, password) {
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {"username": login, "password": password})
            .then(response => {
                let token = response.data.token
                console.log(token)
                localStorage.setItem('token', token)
                this.setState({
                    'token': token
                }, this.getData)
            })
            .catch(error => console.log(error))
    }


    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
    }

    logOut() {
        localStorage.setItem('token', '')
        this.setState({
            'token': ''
        }, this.getData)
    }

    isAuth() {
        return !!this.state.token
    }

    getHeaders() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return {}
    }

    getData() {
        let headers = this.getHeaders()

        axios
            .get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                let users = response.data.results
                this.setState({
                    'users': users
                })
            })
            .catch(error => {
                this.setState({
                'users': []
                })
                console.log(error)
            })


        axios
            .get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                let projects = response.data.results
                this.setState({
                    'projects': projects
                })
            })
            .catch(error => {
                this.setState({
                'projects': []
                })
                console.log(error)
            })

        axios
            .get('http://127.0.0.1:8000/api/todos/', {headers})
            .then(response => {
                let todos = response.data.results
                this.setState({
                    'todos': todos
                })
            })
            .catch(error => {
               this.setState({
               'todos': []
               })
               console.log(error)
            })

        }

        render() {
            return (
                <div>
                    <BrowserRouter>
                        <nav>
                            <li><Link to='/'>Пользователь</Link></li>
                            <li><Link to='/projects'>Проект</Link></li>
                            <li><Link to='/todos'>Заметка</Link></li>
                            <li>
                            { this.isAuth() ? <button onClick={()=>this.logOut()}>Logout</button> : <Link to='/login'>Login</Link> }
                            </li>
                        </nav>

                        <Routes>
                            <Route exact path='/' element = {<UserList users={this.state.users} />} />
                            <Route exact path='/login' element = {<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)}/>} />
                            <Route exact path='/projects' element = {<ProjectList projects={this.state.projects} />} />
                            <Route exact path='/todos' element = {<ToDoList todos={this.state.todos} />} />
                            <Route exact path='/users' element = {<Navigate to='/' />} />
                        </Routes>
                    </BrowserRouter>
                </div>
            )
        }
    }


export default App;

