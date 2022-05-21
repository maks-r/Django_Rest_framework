import React from 'react'


class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': '',
            'name': []
        }
    }

    handleSubmit(event) {
        this.props.createProject(this.state.users, this.state.name)
        event.preventDefault()
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }


     handleProjectChange(event) {
        if (!event.target.selectedOptions) {
            return
        }

        let users = []

        for (let i = 0; i < event.target.selectedOptions.length; i++) {
           users.push(parseInt(event.target.selectedOptions.item(i).value))
        }

        this.setState({
            'users': users
        })
    }

    render() {
        return (
        <form onSubmit={(event) => this.handleSubmit(event)}>
            <input type="text" name="project" placeholder="project" value={this.state.project} onChange={(event) => this.handleChange(event)} />
            <select multiple onChange={(event) => this.handleProjectChange(event)}>
                {this.props.users.map((user) => <option value={user.id}>{user.name}</option>)}
            </select>
            <input type="submit" value="Create"/>
        </form>
        )
    }
}

export default ProjectForm;