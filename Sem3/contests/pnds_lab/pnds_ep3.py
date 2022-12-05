import pandas as pd
import matplotlib.pyplot as plt

students_by_res_frame = pd.read_html('results_ejudge.html', index_col='User')[0][['Solved', 'G', 'H']]
students_by_groups_frame = pd.read_excel('students_info.xlsx', index_col='login')

students_by_res_frame.index.names = ['student']
students_by_groups_frame.index.names = ['student']

students_frame = pd.merge(students_by_res_frame, students_by_groups_frame, on='student')
students_frame = students_frame.rename(str.lower, axis='columns')

best_students_frame = students_frame[(students_frame['g'] > 10) | (students_frame['h'] > 10)]

print('Students from the following groups solved the test best:')
print('Faculty groups: ' + str(set(best_students_frame['group_faculty'])))
print('Out groups: ' + str(set(best_students_frame['group_out'])))

group_faculty_frame = students_frame.groupby('group_faculty').mean()
group_out_frame = students_frame.groupby('group_out').mean()

fig, (ax_faculty_groups, ax_out_groups) = plt.subplots(1, 2)
fig.set_size_inches(10, 6)
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.95,
                    top=0.9,
                    wspace=0.4)

ax_faculty_groups.bar(group_faculty_frame.index, group_faculty_frame['solved'], color='#E87626')
ax_faculty_groups.set_title('Mean solved by faculty groups')
plt.sca(ax_faculty_groups)
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8])

ax_out_groups.bar(group_out_frame.index, group_out_frame['solved'], color='#E82626')
ax_out_groups.set_title('Mean solved by out groups')
plt.sca(ax_out_groups)
plt.xticks([31, 32, 33, 34, 35, 36, 37, 38])

plt.savefig('mean_solved.png', dpi=400)
