import React from "react";
import Header from "../../components/header/header";
import {FormattedMessage} from "react-intl";
import styled from "styled-components";
import LivingProofAPI from "../../repository/api/livingProofAPI";
import Footer from "../../components/footer/footer";
import {Link} from "react-router-dom";


class LivingProofDetail extends React.Component {
  constructor(props) {
    super(props);
    this.state = {livingProofDetail: {}}
  }

  async componentDidMount() {
    const livingProofDetail = await LivingProofAPI.fetchLivingProofDetail(this.livingProofId);
    this.setState({livingProofDetail})
  }

  get livingProofId() {
    return this.props.match.params.id;
  }

  render() {
    const {livingProofDetail} = this.state;
    return (
      <div>
        <Header/>
        <Container>
          <Innner className="ui container">
            <h2 className="ui header red">{livingProofDetail.name}</h2>
            {livingProofDetail.alphabet && <h3 className="ui header black">{livingProofDetail.alphabet}</h3>}
            <img src={livingProofDetail.faceImageURL} className="ui huge image"/>
            <HeaderBox><FormattedMessage id="livingProof.basicData"/></HeaderBox>
            <div className="ui grid">
              {["birthday", "occupation", "motto", "introduction", "postmortemName", "birthplace", "height", "weight"]
                .map((propName, i) => (
                  <Row livingProofDetail={livingProofDetail} propName={propName} key={i}/>))}
            </div>
            <HeaderBox><FormattedMessage id="livingProof.interview"/></HeaderBox>
            <div className="ui grid">
              {["nickname", "livedPlace", "whereBeen", "academicBackground", "personality", "firstLove", "numberInRelationship", "childhoodLonging", "jobTried", "goodAt", "badAt", "favoriteFood", "dislikeFood", "boast", "hobby", "numberDescendants", "predictingDeathCause", "desiredOffering", "unneededOffering", "messageToFamily", "blog", "propose"]
                .map((propName, i) => (
                  <Row livingProofDetail={livingProofDetail} propName={propName} key={i}/>))}
            </div>
            <HeaderBox><FormattedMessage id="livingProof.lifeChart"/></HeaderBox>
            <img className="ui fluid image" src={livingProofDetail.lifeChartImageURL} alt="life chart"/>
            <HeaderBox><FormattedMessage id="livingProof.familyTree"/></HeaderBox>
            <img className="ui fluid image" src={livingProofDetail.familyTreeImageURL} alt="family tree"/>
            <Link to={`/todo-list/${this.livingProofId}`}><HeaderBox>TODO LIST</HeaderBox></Link>
          </Innner>
        </Container>
        <Footer/>
      </div>)
  }
}

const Row = ({livingProofDetail, propName}) => (
  <div className="row">
    <BorderBottom className="six wide column bottom bordered"><FormattedMessage
      id={`livingProof.${propName}`}/></BorderBottom>
    <BorderBottom className="eight wide column">{livingProofDetail[propName]}</BorderBottom>
  </div>
);

const HeaderBox = ({children}) => (
  <HeaderBoxContainer>
    <BlueRectangle/>
    <Title>{children}</Title>
  </HeaderBoxContainer>
);

const Container = styled.div`
  background-color: #FDF5EE;
`;

const Innner = styled.div`
  padding-top: 3vh;
`;
const BorderBottom = styled.div`
  border-bottom: solid;
  border-color: #C2C2C2;
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
export default LivingProofDetail;
