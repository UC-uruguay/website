import React from "react";
import Header from "../../components/header/header";
import styled from "styled-components";
import Footer from "../../components/footer/footer";
import {Select} from 'semantic-ui-react'

class AiKaimyou extends React.Component {
  state = {character: "", hobby: "", inngou: "", ownName: "", respectName: "", rank: 1};

  render() {
    return (
      <div>
        <Header/>
        <Container>
          <div className="ui container">
            <HeaderBox>院号</HeaderBox>
            <div className="ui form">
              <div className="field">
                <label>院号</label>
                <input type="text" name="院号" placeholder="院号" onChange={e => this.setState({inngou: e.target.value})}/>
              </div>
            </div>
            <HeaderBox>道号</HeaderBox>
            <div className="ui form">
              <div className="field">
                <label>性格</label>
                <input type="text" name="性格" placeholder="性格"
                       onChange={e => this.setState({character: e.target.value})}/>
                <label>趣味</label>
                <input type="text" name="趣味" placeholder="趣味" onChange={e => this.setState({hobby: e.target.value})}/>
              </div>
            </div>
            <HeaderBox>戒名</HeaderBox>
            <div className="ui form">
              <div className="field">
                <label>名前</label>
                <input type="text" name="名前" placeholder="名前"
                       onChange={e => this.setState({ownName: e.target.value})}/>
                <label>尊敬する人の名前</label>
                <input type="text" name="尊敬する人の名前" placeholder="尊敬する人の名前"
                       onChange={e => this.setState({respectName: e.target.value})}/>
              </div>
            </div>
            <HeaderBox>位号</HeaderBox>
            <div className="ui form">
              <div className="field">
                <label>年齢</label>
                <Select placeholder='年齢'
                        options={
                          [{key: "1", value: 1, text: "0~1"},
                            {key: "2", value: 2, text: "2~5"},
                            {key: "3", value: 3, text: "6~15"},
                            {key: "4", value: 4, text: "15~"}
                          ]}
                        onChange={(e, data) => this.setState({age: data.value})}/>
                <label>性別</label>
                <Select placeholder='年齢'
                        options={
                          [{key: "1", value: 1, text: "男"},
                            {key: "2", value: 2, text: "女"}
                          ]}
                        onChange={(e, data) => this.setState({gender: data.value})}/>
                <label>ランク</label>
                <Select placeholder='ランク'
                        options={
                          [{key: "1", value: 1, text: "1"},
                            {key: "2", value: 2, text: "2"},
                            {key: "3", value: 3, text: "3"},
                            {key: "4", value: 4, text: "4"}
                          ]}
                        onChange={(e, data) => this.setState({rank: data.value})}/>
              </div>
            </div>
            <HeaderBox>あなたの戒名は</HeaderBox>
            <Decorated>{this.getFullKaimyou()}</Decorated>
          </div>
        </Container>
        <Footer/>
      </div>)
  }

  getFullKaimyou() {
    return this.getInngou() + this.getDougou() + this.getKaimyou() + this.getIgou();
  }

  getInngou() {
    return this.state.inngou;
  }

  getDougou() {
    return getKanji(this.state.character) + getKanji(this.state.hobby)
  }

  getKaimyou() {
    return getKanji(this.state.respectName) + getKanji(this.state.ownName)
  }

  getIgou() {
    const {age, gender, rank} = this.state;
    if (age === 0) {
      return ""
    } else if (age === 1) {
      return gender === 2 ? "嬰女" : "嬰子"
    } else if (age === 2) {
      return gender === 2 ? "幼女" : "幼子"
    } else if (age === 3) {
      return gender === 2 ? "童女" : "童子"
    } else if (age === 4) {
      if (rank === 1) {
        return gender === 2 ? "信女" : "信士"
      } else if (rank === 2) {
        return gender === 2 ? "大姉" : "居士"
      } else if (rank === 3) {
        return gender === 2 ? "清大姉" : "清居士"
      } else if (rank === 4) {
        return gender === 2 ? "院大姉" : "院居士"
      }
    }
    return ""
  }
}

const getKanji = (str) => {
  const kanjis = str.split("").filter(s => s.match(/[\u4E00-\u9FFF]/));
  return kanjis[Math.floor(Math.random() * kanjis.length)] || "";
};

const HeaderBox = ({children}) => (
  <HeaderBoxContainer>
    <BlueRectangle/>
    <Title>{children}</Title>
  </HeaderBoxContainer>
);

const Decorated = styled.div`
  font-size: 3rem;
`;
const HeaderBoxContainer = styled.div`
  margin-top: 5vh;
  margin-bottom: 3vh;
  background-color: #EEEEEE;
  height: 5vh;
  display: flex;
  justify-content: flex-start;
  align-items: center;
`;
const BlueRectangle = styled.div`
  background-color: #2C3882;
  width: 1vw;
  height: 4vh;
  margin-right: 4vw;
`;
const Title = styled.div`
  display: flex;
  justify-content: flex-start;
  align-items: center;
  font-size: 2rem;
`;
const Container = styled.div`
  background-color: #FDF5EE;
  padding-top: 5vh;
  padding-bottom: 7vh;
`;

export default AiKaimyou;
