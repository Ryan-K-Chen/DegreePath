import React from "react";
import { DragSource } from "react-dnd";
import { Button, Col, Card, Modal } from "antd";
import { MovableTypes } from "./MovableTypes";
import { InfoCircleOutlined } from "@ant-design/icons";
import _ from "lodash";
import 'antd/dist/antd.css';

import courses_dictionary from "./data/courses_dictionary.json"

const spec = {
    beginDrag(props, monitor, component) {
        props.onDrag(props.name);
        return component.props;
    }
}

const collect = (connect, monitor) => {
    return {
        connectDragSource: connect.dragSource()
    }
}

export const Class = DragSource(MovableTypes.CLASS, spec, collect) (class extends React.Component {
    constructor(props){
        super(props);
        console.log(courses_dictionary)
        let hours = {};
        _.forEach(courses_dictionary[this.props.name]["Hours"], (value, key) => {
            hours[key] = parseFloat(value);
        });
        this.hours = (Object.keys(hours).map(c => (
            c + ": " + hours[c]
        ))).toString().replace(/,/g, "  |  ");
        console.log(this.hours);
        this.state = {
            showmodal: false
        }
    }
    render(){
        const {connectDragSource} = this.props;
        return (connectDragSource(
            <div>
                <Col>
                    <Card onClick={()=>{this.showModal()}} style={{width: 200, backgroundColor: '#B4A76C'}} bordered={false} hoverable>
                        <h2>
                            <b>
                                <center>
                                    {this.props.name}
                                </center>
                            </b>
                        </h2>
                    </Card>
                </Col>
                <Modal 
                    visible={this.state.modalState}
                    onOk={()=>{this.hideModal()}}
                    onCancel={()=>{this.hideModal()}}
                    footer={[
                        <div style={{
                            whiteSpace: "pre-wrap"
                        }}>
                            {this.hours}
                        </div>
                    ]}
                >
                    <h2>
                        <b>
                            <center>
                                {this.props.name}: {courses_dictionary[this.props.name]["Course Title"]}
                            </center>
                        </b>
                    </h2>
                    <p>
                        {courses_dictionary[this.props.name]["Description"]}
                    </p>
                </Modal>
            </div>
        ));
    }
    showModal(){
        console.log("hello")
        this.setState({
            modalState: true
        });
    }
    hideModal(){
        this.setState({
            modalState: false
        })
    }
});
