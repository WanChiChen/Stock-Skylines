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

const handleFormSubmit = async () => {
  const response = await post("/api/", {
    ticker: "MAR",
    period: "1d",
    start: "2010-10-01",
    end: "2020-12-31",
    ratio: "0.8"
  });

  let data = JSON.parse(response.data);
  let keys = Object.keys(data);
  let stock_price = data[keys[0]];
  let city_price = data[keys[1]];

  Object.keys(stock_price).forEach(date => {
    let utc = new Date(0);
    utc.setUTCMilliseconds(date)
    console.log(utc)
  })
}
export default function Dashboard() {
  const classes = useStyles();
  console.log(dailySalesChart.data)
  return (
    <div>
          <Button onClick={handleFormSubmit}>

          </Button>
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
                data={dailySalesChart.data}
                type="Line"
                options={dailySalesChart.options}
                listener={dailySalesChart.animation}
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
