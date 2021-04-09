import React from 'react';
import ReactDOM from 'react-dom';

class Members extends React.Component {
    state = {
        members_count: []
    }

    componentDidMount() {
        const apiURL = 'http://backend-env.eba-w6ysmk2u.us-east-2.elasticbeanstalk.com/members_count';
        fetch(apiURL)
            .then((response) => response.json())
            .then((data) => this.setState({members_count: data[0]}));
    }

    render() {
        return <h2>Total Members: {this.state.members_count}</h2>;
    }
}

ReactDOM.render(
    <Members />,
    document.getElementById('root')
);

