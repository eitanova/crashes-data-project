### Data acquisition
Following the retrieval of data through the public API and performing necessary data manipulations, I stored the acquired data in a DataFrame object.

### Parameters table
|  Parameter name   | Parameter value |                    Description                     |
|:-----------------:|:---------------:|:--------------------------------------------------:|
|      weather      |     Integer     |           weather when accident occurred           |
|       city        |     string      |                     City name                      |
|       year        |     Integer     |                      The year                      |
|       month       |     Integer     |                     The month                      |
|     day_type      |     Integer     |  The type of day referred to holiday for example   | 
|     day_time      |     Integer     |   If the accident occurred in day(1) or night(5)   |
|        day        |     Integer     |                The day of the week                 |
| accident_severity |     Integer     | Severity of the accident, from 1(worst) to 3(easy) |
|   accident_type   |     Integer     |             Which type of the accident             |


#### weather values & meaning table
| value |  meaning  |
|:-----:|:---------:|
|   1   |   Sunny   | 
|   2   |   Rainy   |
|   3   | Extra hot |
|   4   |   Foggy   |
|   5   |   Other   | 
|   9   |  Unknown  |

#### day_type values & meaning table
| value |    meaning    |
|:-----:|:-------------:|
|   1   |    Holiday    |
|   2   | Holiday night |
|   3   | Jewish retual |
|   4   |     Other     |

#### accident_type values & meaning table
| value |          meaning           |
|:-----:|:--------------------------:|
|   1   |      Hit with walker       |
|   8   |      Hit with object       |
|   9   |  Went down from the road   |
|  10   |          Rollover          |
|  11   |            Slip            |
|  14   |            Burn            |
|  19   |      Hit with animal       |
|  20   | Injury from a vehicle load |
| Other |   Accident with vehicle    |



