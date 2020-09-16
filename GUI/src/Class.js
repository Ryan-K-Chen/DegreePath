import React from "react";
import { DragSource } from "react-dnd";
import { Button, Col, Card, Modal, Popover } from "antd";
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
        let hours = {};
        _.forEach(courses_dictionary[this.props.name]["Hours"], (value, key) => {
            hours[key] = parseFloat(value);
        });
        this.hours = (Object.keys(hours).map(c => (
            c + ": " + hours[c]
        ))).toString().replace(/,/g, "  |  ");
        this.state = {
            modalState: false,
            popState: false
        }
    }
    render(){
        const {connectDragSource} = this.props;
        let cardStyle = {
            width: 200, 
            backgroundColor: "#B4A76C"
        };

        if(this.props.notsatisfied == true) {
            cardStyle["backgroundColor"] = '#CA4949';
        }
        return (connectDragSource(
            <div>
                <Popover content={
                    <div>
                        {courses_dictionary[this.props.name]["Course Title"]}
                    </div>
                }>
                    <Col>
                        <Card onClick={()=>{this.showModal()}} bordered={false} hoverable onMouseEnter={()=>{console.log("entered")}} onMouseLeave={()=>{console.log("left")}} style={cardStyle} >
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
                                    <a href={courses_dictionary[this.props.name]["url"]} target="_blank">
                                        {this.props.name}: {courses_dictionary[this.props.name]["Course Title"]}
                                    </a>
                                </center>
                            </b>
                        </h2>
                        <p>
                            {courses_dictionary[this.props.name]["Description"]}
                        </p>
                    </Modal>
                </Popover>
            </div>
        ));
    }
    showPop(){
        this.setState({
            popState: true
        });
    }
    hidePop(){
        this.setState({
            popState: false
        });
    }
    showModal(){
        this.setState({
            modalState: true
        });
    }
    hideModal(){
        this.setState({
            modalState: false
        });
    }
});
