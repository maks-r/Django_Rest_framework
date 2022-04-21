import React from 'react'
import axios from 'axios'
import UserList from './components/UserList.js'
import ProjectList from './components/ProjectList.js'
import ToDoList from './components/ToDoList.js'
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation} from 'react-router-dom'


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': []
        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                let users = response.data.results
                this.setState({
                    'users': users
                })
            })
            .catch(error => console.log(error))

            axios
            .get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                let projects = response.data.results
                this.setState({
                    'projects': projects
                })
            })
            .catch(error => console.log(error))

            axios
            .get('http://127.0.0.1:8000/api/todos/')
            .then(response => {
                let todos = response.data.results
                this.setState({
                    'todos': todos
                })
            })
            .catch(error => console.log(error))
        }

        render() {
            return (
                <div>
                    <BrowserRouter>
                        <nav>
                            <li><Link to='/'>Пользователь</Link></li>
                            <li><Link to='/projects'>Проект</Link></li>
                            <li><Link to='/todos'>Заметка</Link></li>
                        </nav>

                        <Routes>
                            <Route exact path='/' element = {<UserList users={this.state.users} />} />
                            <Route exact path='/projects' element = {<UserList users={this.state.users} />} />
                            <Route exact path='/todos' element = {<UserList users={this.state.users} />} />
                        </Routes>
                    </BrowserRouter>
                </div>
            )
        }
    }


export default App;

