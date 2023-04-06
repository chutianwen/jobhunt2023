''' You are planning out a trek across a snowy mountain. On the mountain it snows in the morning, the snow melts with the sun in the afternoon, and in the evening you can attempt a crossing.

* Snow piles up at each location, making that location higher.
* If it has not snowed at a particular location for 2 days, the snow there starts melting on the afternoon of the second day, at a rate of one unit per day.
* You can climb up and down one level while moving to the next position.
* The player needs to cross the mountain with the least amount of climbing possible.
* The crossing attempts are limited to the days in the forecast because the weather is unpredictable later.

Write a function that calculates the best day to perform the crossing and the number of climbs needed, given the base altitude of locations on the mountain and a list of snow forecasts for each day.

For example, given the initial altitudes: [0,1,2,1]

           3
  altitude 2     -
           1   -   -      Side view of the mountain
           0 -
             0 1 2 3
             position

And the snow forecast for each morning:

 [[1,0,1,0],   # On day zero, one unit of snow will fall on positions 0 and 2.

  [0,0,0,0],   # On day one, it will not snow.

  [1,1,0,2]]   # On day two, two units of snow will fall on position 3, and one unit on positions 0 and 1.

This is the resulting mountain profile each evening, the player is represented by the letter P:

            Day 0            Day 1            Day 2

                                           starts melting
                                                 ↓
          3     *                          3 P     *
altitude  2 P   -          no new snow     2 * * - *
          1 * -   -                        1 * -   -
          0 -              no melting      0 -
            0 1 2 3                          0 1 2 3

            position                        position


In the example above:
At the end of day 0, the mountain cannot be crossed. The steps are too high to climb.
At the end of day 1, there are no changes, still no crossing.
At the end of day 2, the mountain can be crossed by climbing once. Notice that in position 2, one unit of snow melted.

In case it's not possible to cross on any of the days, the function should return Null or [-1,-1].

Expected results:

best_day_to_cross(altitudes_1, snow_1) -> [2, 1] at the end of day two, only one climb is required
best_day_to_cross(altitudes_2, snow_2) -> [0, 0] day zero is the best day to cross
best_day_to_cross(altitudes_3, snow_3) -> [2, 0] zero climbs are required at the end of day two
best_day_to_cross(altitudes_4, snow_4) -> [-1,-1] no viable days, the steps are always too high
best_day_to_cross(altitudes_5, snow_5) -> [5, 1] melting can continue over a few days
best_day_to_cross(altitudes_6, snow_6) -> [0, 4] it requires 4 climbs

Complexity variables:

A - number of altitude positions
D - number of days in the forecast '''


def best_day_to_cross(altitude, snows):

    min_num_step, best_day = -1, -1
    remain_snow = [0] * len(altitude)

    for day_idx, snow in enumerate(snows):
        cur_altitude = []
        for step_idx, step_snow in enumerate(snow):
            if step_snow > 0:
                remain_snow[step_idx] += step_snow
            elif step_snow == 0:
                # check previous day if snow
                if day_idx > 0 and snows[day_idx-1][step_idx] == 0 and remain_snow[step_idx] > 0:
                    remain_snow[step_idx] -= 1

            cur_altitude.append(altitude[step_idx] + remain_snow[step_idx])

        print(f'remaining_snow:{remain_snow}, cur_altitude:{cur_altitude}')
        num_step = traverse(cur_altitude)

        if num_step >= 0:
            if min_num_step == -1 or min_num_step > num_step:
                min_num_step = num_step
                best_day = day_idx

    return min_num_step, best_day


def traverse(altitude):
    # print(altitude)
    num_steps = 0
    pre_height = altitude[0]

    for height in altitude[1:]:
        height_diff = abs(height - pre_height)
        if height_diff > 1:
            return -1
        elif height_diff == 1:
            num_steps += 1

        pre_height = height

    return num_steps


altitudes_1 = [0,1,2,1]
snow = [
    [1,0,1,0],
    [0,0,0,0],
    [1,1,0,2]]
print(best_day_to_cross(altitudes_1, snow))












