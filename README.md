# DATA260P Project 2: Bin Packing Algorithms

*View the notebook here:* https://connormcmanigal.github.io/bin-packing-analysis/report.pdf

### Connor McManigal and Aaron Mui

- Implemented next fit, first fit, best fit, first fit decreasing, and best fit decreasing
- Created two custom bin packing algorithms using different packing strategies to improve upon next fit, first fit, and best fit
- Tested algorithms on 5 unique initializations of radom generated data from sizes 100, 200, 400, 800, 1600, 3200, 6400, 12800, and 25600
- Measured waste by comparing optimal number of bins(sum of contents/bin size) with number of bins used
- Took runtime measurements to later approximate implementation based Big-O's
- Graphed waste and runtime performances on log-log scale to determine the estimated functions of waste and runtime
- Used statsmodels and OLS to gather estimated coefficients for waste and runtime
- Provided detailed write up(project2_report.pdf) illustrating our work, plots, and results
