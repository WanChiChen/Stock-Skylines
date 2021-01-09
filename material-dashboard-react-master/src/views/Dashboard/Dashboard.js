import React from "react";
// react plugin for creating charts
import ChartistGraph from "react-chartist";
// @material-ui/core
import { makeStyles } from "@material-ui/core/styles";

// @material-ui/icons
import ArrowUpward from "@material-ui/icons/ArrowUpward";
import AccessTime from "@material-ui/icons/AccessTime";
import Accessibility from "@material-ui/icons/Accessibility";

// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Table from "components/Table/Table.js";
import Tasks from "components/Tasks/Tasks.js";
import CustomTabs from "components/CustomTabs/CustomTabs.js";
import Button from "components/CustomButtons/Button.js";
import Danger from "components/Typography/Danger.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardIcon from "components/Card/CardIcon.js";
import CardBody from "components/Card/CardBody.js";
import CardFooter from "components/Card/CardFooter.js";
import { Line } from 'react-chartjs-2'


import { bugs, website, server } from "variables/general.js";
import {post} from "utils/fetchService.js";

import {
  dailySalesChart,
  emailsSubscriptionChart,
  completedTasksChart
} from "variables/charts.js";

import styles from "assets/jss/material-dashboard-react/views/dashboardStyle.js";

const useStyles = makeStyles(styles);

export default function Dashboard(props) {
  const classes = useStyles();

  React.useEffect(() => {

    async function get_response(props) {
      let ret = await post("/api/", {
        ticker: props.inputState.ticker,
        period: "1d",
        start: props.inputState.start,
        end: props.inputState.end,
        ratio: "0.8"
      });

      if (ret.errors)
        return;

      let stockPriceArray = []
      let cityPriceArray = []
      let dateArray = []

      let data = JSON.parse(ret.data);
      let keys = Object.keys(data);
      let stock_price = data[keys[0]];
      let city_price = data[keys[1]];
    
      Object.keys(stock_price).forEach(date => {
        let utc = new Date(0);
        utc.setUTCMilliseconds(date)
        utc = utc.toLocaleDateString()
        dateArray.push(utc)
    
        stockPriceArray.push(stock_price[date])
        cityPriceArray.push(city_price[date])
      })
    
      let retData = {
        labels: dateArray,
        datasets: [
        {
          label: keys[0],
          data: stockPriceArray,
          backgroundColor: 'rgba(75,192,192,0.4)',
          borderColor: 'rgba(75,192,192,1)',
        },
        {
          label: keys[1],
          data: cityPriceArray,
          backgroundColor: 'rgba(165, 255, 140,0.4)',
          borderColor: 'rgba(165, 255, 140,1)',
        }
      ]}
    
      setState({data: retData, ticker: keys[0], city: keys[1]});
    }
     get_response(props); 
  },[props.inputState])
  
  const [state, setState] = React.useState({
    data: [],
    ticker: '',
    city: '',
  });

  return (
    <div>
          
          <Card chart>
            <CardBody>
              <h4 className={classes.cardTitle}>Daily Sales</h4>
              <p className={classes.cardCategory}>
                <span className={classes.successText}>
                  <ArrowUpward className={classes.upArrowCardCategory} /> 55%
                </span>{" "}
                increase in today sales.
              </p>
            </CardBody>
            <Line
                className="ct-chart"
                data={state.data}
                type="Line"
              />
            <CardFooter chart>
              <div className={classes.stats}>
                <AccessTime /> updated 4 minutes ago
              </div>
            </CardFooter>
          </Card>
    </div>
  );
}
