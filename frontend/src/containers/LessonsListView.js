import React from 'react';
import axios from 'axios';
import Lesson from '../components/Lesson';
import CreateLessonForm from '../components/Form';

class LessonsList extends React.Component {

    state = {
        lessons: [],
    }

    componentDidMount() {
        axios.get('http://localhost:8000/api/')
            .then(res => {
                this.setState({
                    lessons: res.data,
                });
            })
            .then(console.log(this.lessons))
    }
    render() {
        return (
            <div>
                <Lesson data={this.state.lessons} />
                <br />

                <h2>Създайте урок</h2>
                <CreateLessonForm />
            </div>
        );
    }
}

export default LessonsList;