from real_time_engine.constraint.constraint import ConstraintManager, BaseConstraint
import real_time_engine.datastores as datastores
import pandas as pd
import datetime as dt

@ConstraintManager.register_constraint
class ZoneLateConstraint(BaseConstraint):

    def __init__(self, config: any,
                 end_date=str(dt.datetime.now().date() - dt.timedelta(days=1))):
        self._config = config
        self._df = pd.DataFrame()
        self._start_date = str(dt.datetime.strptime(end_date, '%Y-%m-%d').date() -
                               dt.timedelta(days=self._config.DAYS - 1))
        self._end_date = end_date
        self._calculate_constraint()

    def _get_data(self):
        df = datastores.snowflake.dataframe(filename=self._config.SQL_FILE,
             start_date=self._start_date,
             end_date=self._end_date
        )
        return df

    def _calculate_constraint(self):
        df = self._get_data()

        df_daily = df[['date', 'late_orders', 'tot_orders']].groupby('date').sum() \
            .reset_index().rename(columns={'late_orders': 'daily_lates',
                                           'tot_orders': 'daily_totals'})
        df_daily['daily_late_pct'] = df_daily['daily_lates'] / df_daily['daily_totals']
        df = df.merge(df_daily[['date', 'daily_late_pct']],
                      on=['date'])

        df_constraint = df[df['daily_late_pct'] < self._config.THRESHOLDS.daily_late_threshold]
        df_constraint = df_constraint[['zone_id', 'late_percent']].groupby('zone_id').median().reset_index()
        df_constraint['capped_late'] = df_constraint['late_percent']
        df_constraint.loc[df_constraint['late_percent'] > self._config.THRESHOLDS.zone_late_cap_higher,
                          'capped_late'] = self._config.THRESHOLDS.zone_late_cap_higher
        df_constraint.loc[df_constraint['late_percent'] < self._config.THRESHOLDS.zone_late_cap_lower,
                          'capped_late'] = self._config.THRESHOLDS.zone_late_cap_lower
        self._df = df_constraint[['zone_id', 'capped_late']]

    def get_constraint(self, zone_id):
        return self._df[self._df['zone_id'] == zone_id]['capped_late'].values[0]