import React from "react";
// import {FormattedMessage} from "react-intl";
import styled from "styled-components";
import LivingProofAPI from "../../repository/api/livingProofAPI";
import mediaQuery from "styled-media-query";
import Header from "../../components/header/header";
import Footer from "../../components/footer/footer";
import {Draggable, Droppable, DragDropContext} from 'react-beautiful-dnd';


class TodoList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      tasks: {},
      todo: {
        items: []
      },
      done: {
        items: []
      }
    }
  }

  async componentDidMount() {
    // const todoList = await LivingProofAPI.fetchTodoList(this.livingProofId);
    // this.setState({todoList})
    this.setState({
        tasks: {
          1: {id: 1, title: "title1", description: "description1"},
          2: {id: 2, title: "title2", description: "description2"},
          3: {id: 3, title: "title3", description: "description3"},
          4: {id: 4, title: "title4", description: "description4"},
        },
        todo: {
          items: [1, 2]
        },
        done: {
          items: [4, 3]
        },
        title: "",
        description: ""
      }
    )
  }

  get livingProofId() {
    return this.props.match.params.id;
  }

  addTodo = () => {
    const {title, description, tasks, todo} = this.state;
    const newTaskId = Math.max(...[0, ...Object.keys(tasks)]) + 1;
    this.setState({
      tasks: {...tasks, [newTaskId]: {id: newTaskId, title, description}},
      todo: {items: [newTaskId, ...todo.items]}
    })
  };

  onDragend = result => {
    const {source, destination, draggableId} = result;
    if (!destination) return;
    if (destination.droppableId === source.droppableId && destination.index === source.index) return;
    if (destination.droppableId === source.droppableId) {
      //reorder array
      const newItems = Array.from(this.state[destination.droppableId].items);
      newItems.splice(source.index, 1);
      newItems.splice(destination.index, 0, parseInt(draggableId))
      this.setState({[destination.droppableId]: {items: newItems}})
    } else if (destination.droppableId !== source.droppableId) {
      //delete from src array
      const srcNewItems = Array.from(this.state[source.droppableId].items);
      srcNewItems.splice(source.index, 1);
      //insert into dest array
      const destNewItem = Array.from(this.state[destination.droppableId].items);
      destNewItem.splice(destination.index, 0, parseInt(draggableId));
      this.setState({[source.droppableId]: {items: srcNewItems}, [destination.droppableId]: {items: destNewItem}})
    }
  };

  render() {
    const {todo, done, tasks, createNew, title, description} = this.state;
    return (
      <div>
        <Header/>
        <Container>
          <Innner className="ui container">
            <DragDropContext onDragEnd={this.onDragend}>
              <h1>TODO</h1>
              <Droppable droppableId="todo" direction="horizontal">
                {provided => (
                  <TaskList
                    ref={provided.innerRef}
                    {...provided.droppableProps}
                  >
                    <Cards className="ui cards">
                      {createNew ?
                        (<Card className="card">
                          <div className="content">
                            <form className="ui form">
                              <div className="header">
                                <input
                                  type="text"
                                  placeholder="title"
                                  defaultValue={title}
                                  onChange={e => {
                                    e.preventDefault();
                                    this.setState({title: e.target.value})
                                  }}/>
                              </div>
                              <div className="description">
                                <input type="text"
                                       placeholder="description"
                                       defaultValue={description}
                                       onChange={e => {
                                         e.preventDefault();
                                         this.setState({description: e.target.value})
                                       }}/>
                              </div>
                            </form>
                          </div>
                          <div className="ui bottom attached button" onClick={this.addTodo}>
                            <i className="add icon"/>
                            Add Todo
                          </div>
                        </Card>) :
                        (<Card className="card" onClick={() => {
                          this.setState({createNew: true})
                        }} style={{background: "url(/images/todo/add-todo.png)"}}/>)}
                      {todo && todo.items && todo.items.map((todoId, index) => {
                        const item = tasks[todoId];
                        if (!item) return <div key={index}/>;
                        return <Draggable key={item.id} draggableId={"" + item.id} index={index}>
                          {(provided) => (
                            <Card className="card" {...provided.draggableProps} {...provided.dragHandleProps}
                                  ref={provided.innerRef}>
                              <div className="content">
                                <div className="header">{item.title}</div>
                                <div className="description">
                                  {item.description}
                                </div>
                              </div>
                            </Card>)}
                        </Draggable>
                      })}
                    </Cards>
                    {provided.placeholder}
                  </TaskList>)}
              </Droppable>
              <h1>DONE</h1>
              <Droppable droppableId="done" direction="horizontal">
                {provided => (
                  <TaskList
                    ref={provided.innerRef}
                    {...provided.droppableProps}
                  >
                    <Cards className="ui cards">
                      {done && done.items && done.items.map((doneId, index) => {
                        const item = tasks[doneId];
                        if (!item) return <div key={index}/>;
                        return <Draggable key={item.id} draggableId={"" + item.id} index={index}>
                          {(provided) => (
                            <Card className="card" {...provided.draggableProps} {...provided.dragHandleProps}
                                  ref={provided.innerRef}>
                              <div className="content">
                                <div className="header">{item.title}</div>
                                <div className="description">
                                  {item.description}
                                </div>
                              </div>
                            </Card>)}
                        </Draggable>
                      })}
                    </Cards>
                    {provided.placeholder}
                  </TaskList>)}
              </Droppable>
            </DragDropContext>
          </Innner>
        </Container>
        <Footer/>
      </div>)
  }
}

const TaskList = styled.div`
`;

const mediaMobile = mediaQuery.lessThan("medium");

const Container = styled.div`
  background-color: #FDF5EE;
`;

const Innner = styled.div`
  padding-top: 3vh;
`;
const Card = styled.div`
  width: 290px;
  height: 200px !important;
  ${mediaMobile`width: 100px;`}
  ${mediaMobile`height: 100px;`}
`;
const Cards = styled.div`
  min-height: 36.5vh;
`;

const UploadIcon = styled.i`
  font-size: 80px;
  ${mediaMobile`font-size: 40px;`}
  color: white;
`;


export default TodoList;
