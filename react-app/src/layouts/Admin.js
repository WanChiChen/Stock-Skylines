import React from "react";
import { Switch, Route, Redirect } from "react-router-dom";
import DateFnsUtils from "@date-io/date-fns";
// creates a beautiful scrollbar
import PerfectScrollbar from "perfect-scrollbar";
import "perfect-scrollbar/css/perfect-scrollbar.css";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
// core components
import Grid from "@material-ui/core/Grid";
import Navbar from "components/Navbars/Navbar.js";
import Footer from "components/Footer/Footer.js";
import CardBody from "components/Card/CardBody.js";
import Card from "components/Card/Card";
import Sidebar from "components/Sidebar/Sidebar.js";
import DashboardPage from "views/Dashboard/Dashboard.js";
import TextField from "@material-ui/core/TextField";
import routes from "routes.js";
import Button from "@material-ui/core/Button";

import styles from "assets/jss/material-dashboard-react/layouts/adminStyle.js";

import bgImage from "assets/img/sidebar-2.jpg";
import logo from "assets/img/reactlogo.png";

import {
  MuiPickersUtilsProvider,
  KeyboardTimePicker,
  KeyboardDatePicker,
} from "@material-ui/pickers";

let ps;

function formatDate(date) {
  var d = new Date(date),
    month = "" + (d.getMonth() + 1),
    day = "" + d.getDate(),
    year = d.getFullYear();

  if (month.length < 2) month = "0" + month;
  if (day.length < 2) day = "0" + day;

  return [year, month, day].join("-");
}

const useStyles = makeStyles(styles);

export default function Admin({ ...rest }) {
  // styles
  const classes = useStyles();
  // ref to help us initialize PerfectScrollbar on windows devices
  const mainPanel = React.createRef();
  // states and functions
  const [image, setImage] = React.useState(bgImage);
  const [color, setColor] = React.useState("blue");
  const [fixedClasses, setFixedClasses] = React.useState("dropdown show");
  const [mobileOpen, setMobileOpen] = React.useState(false);

  const [selectedStartDate, setSelectedStartDate] = React.useState(
    new Date("2020-01-02")
  );
  const [selectedEndDate, setSelectedEndDate] = React.useState(
    new Date("2021-01-02")
  );

  const tickerRef = React.useRef();

  const handleSubmit = () => {
    setState({
      ticker: tickerRef.current.value,
      start: formatDate(selectedStartDate),
      end: formatDate(selectedEndDate),
    });
  };

  const handleStartDateChange = (date) => {
    setSelectedStartDate(date);
  };

  const handleEndDateChange = (date) => {
    setSelectedEndDate(date);
  };

  const [state, setState] = React.useState({
    ticker: "",
    start: "",
    end: "",
  });

  const handleImageClick = (image) => {
    setImage(image);
  };
  const handleColorClick = (color) => {
    setColor(color);
  };
  const handleFixedClick = () => {
    if (fixedClasses === "dropdown") {
      setFixedClasses("dropdown show");
    } else {
      setFixedClasses("dropdown");
    }
  };
  const getRoute = () => {
    return window.location.pathname !== "/admin/maps";
  };
  const resizeFunction = () => {
    if (window.innerWidth >= 960) {
      setMobileOpen(false);
    }
  };
  // initialize and destroy the PerfectScrollbar plugin
  React.useEffect(() => {
    if (navigator.platform.indexOf("Win") > -1) {
      ps = new PerfectScrollbar(mainPanel.current, {
        suppressScrollX: true,
        suppressScrollY: false,
      });
      document.body.style.overflow = "hidden";
    }
    window.addEventListener("resize", resizeFunction);
    // Specify how to clean up after this effect:
    return function cleanup() {
      if (navigator.platform.indexOf("Win") > -1) {
        ps.destroy();
      }
      window.removeEventListener("resize", resizeFunction);
    };
  }, [mainPanel]);

  return (
    <div className={classes.wrapper}>
      <Sidebar
        routes={routes}
        logoText={"Stock Skylines"}
        logo={logo}
        image={image}
        open={mobileOpen}
        color={color}
        {...rest}
      />
      <div className={classes.mainPanel} ref={mainPanel}>
        {/* On the /maps route we want the map to be on full screen - this is not possible if the content and conatiner classes are present because they have some paddings which would make the map smaller */}
        <div className={classes.content}>
          <div className={classes.container}>
            <Card>
              <CardBody>
                <Grid container alignItems="center" justify="center">
                  <Grid item>
                    <TextField
                      id="ticker"
                      defaultValue="TSLA"
                      label="Stock ticker"
                      margin="none"
                      inputRef={tickerRef}
                    />
                  </Grid>
                  <MuiPickersUtilsProvider utils={DateFnsUtils}>
                    <KeyboardDatePicker
                      disableToolbar
                      variant="inline"
                      format="yyyy/MM/dd"
                      margin="none"
                      id="start"
                      label="Start Date"
                      onChange={handleStartDateChange}
                      value={selectedStartDate}
                      KeyboardButtonProps={{
                        "aria-label": "change date",
                      }}
                    />
                    <KeyboardDatePicker
                      disableToolbar
                      variant="inline"
                      format="yyyy/MM/dd"
                      margin="none"
                      id="end"
                      label="End Date"
                      onChange={handleEndDateChange}
                      value={selectedEndDate}
                      KeyboardButtonProps={{
                        "aria-label": "change date",
                      }}
                    />
                  </MuiPickersUtilsProvider>
                  <Grid item>
                    <Button onClick={handleSubmit} variant="contained">
                      Submit
                    </Button>
                  </Grid>
                </Grid>
              </CardBody>
            </Card>
          </div>
          <div className={classes.container}>
            <DashboardPage inputState={state} />
          </div>
        </div>
      </div>
    </div>
  );
}
