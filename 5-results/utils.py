import altair as alt

LANGS_2_MAPPING = {
    "en": "English",
    "ru": "Russian",
    "tr": "Turkish",
    "id": "Indonesian",
    "zh": "Chinese",
    "fa": "Persian",
    "ko": "Korean",
    "el": "Greek",
    "he": "Hebrew",
    "vi": "Vietnamese",
    "ja": "Japanese",
}

color_mapping = {
    'Chinese': '#1f77b4',
    'English': '#ff7f0e',
    'Greek': '#2ca02c',
    'Hebrew': '#d62728',
    'Indonesian': '#9467bd',
    'Japanese': '#8c564b',
    'Korean': '#e377c2',
    'Persian': '#7f7f7f',
    'Russian': '#bcbd22',
    'Turkish': '#17becf',
    'Vietnamese': '#d2b48c'
}


def get_accuracy_chart(lang_df,  
                       title="", 
                       domain=[0,100],
                       width=150,
                       height=150):
    lang_df = lang_df.sort_values('Step')
    lang_df['Step'] = lang_df['Step'].astype(str)
    lang_df["Language"] = lang_df["Language"].map(LANGS_2_MAPPING)
    
    
    return alt.Chart(lang_df).mark_line(point=True).encode(
        x=alt.X(
            'Step', 
            sort=None, 
            axis=alt.Axis(
                title="Checkpoint Step",
                labelAngle=30
            )
        ),
        y=alt.Y('Accuracy', scale=alt.Scale(domain=domain)),
        color="Task",
        tooltip=['Task', 'Language', 'Accuracy', 'Step', 'Tokens']
    ).properties(
        title=title,
        width=width,
        height=height
    ).interactive()
    
def plot_best_fit_curve(data_points, 
                        fit_data, 
                        lang,
                        width=150, 
                        height=150):
    curve = alt.Chart(fit_data).mark_line(
    ).encode(
        x=alt.X(
            "Checkpoint Step:Q",
            sort=None,
            axis=alt.Axis(labels=True),
            scale=alt.Scale(domain=[-0.1,4.1])
        ),
        y=alt.Y(
            "Accuracy (normalized):Q",
            axis=alt.Axis(labels=False),
            scale=alt.Scale(domain=[-0.1,1.1])
        ),
        color='Task:N'
    ).properties(
        width=width,
        height=height        
    ).interactive()
    
    points = alt.Chart(data_points).mark_point(
    ).encode(
        x=alt.X(
            "N",
            sort=None,
            axis=alt.Axis(labels=True),
            scale=alt.Scale(domain=[-0.1,4.1])   
        ),
        y=alt.Y(
            "Accuracy (normalized):Q",
            scale=alt.Scale(domain=[-0.1,1.1])
        ),
        color="Task:N",
        tooltip=[
            "Task:N",
            "Accuracy",
            "Accuracy (normalized):Q",
            "Step:Q",
            "Tokens:N",
        ],
    ).properties(
        width=width,
        height=height        
    ).interactive()
        
    chart = (curve + points).properties(
        title=LANGS_2_MAPPING[lang]
    )
    return chart

def get_charts_for_langs(langs, 
                        df, 
                        fit_df, 
                        domain=[0,100],
                        height=150,
                        width=150):
    charts = []
    for lang in langs:
        charts.append(alt.hconcat(
                    get_accuracy_chart(
                        df[df['Language'] == lang],
                        title=LANGS_2_MAPPING[lang], 
                        domain=domain,
                        height=height,
                        width=width
                        ), 
                    plot_best_fit_curve(
                        df[df['Language'] == lang],
                        fit_df[fit_df['Language'] == lang],
                        lang,
                        height=height,
                        width=width
                        ),
                    )
                )
    return charts

def get_charts_for_tasks(tasks, 
                         df, 
                         fit_df, 
                         x_domain=[-0.2,4.2],
                         y_domain=[-0.2, 1.1],
                         height=150, 
                         width=150):
    charts = []
    for task in tasks:
        filtered_df = df[df['Task'] == task].copy()
        filtered_df["Language"] = filtered_df["Language"].map(LANGS_2_MAPPING)
        filtered_fit_df = fit_df[fit_df['Task'] == task].copy()
        filtered_fit_df["Language"] = filtered_fit_df["Language"].map(LANGS_2_MAPPING)
        
        
        curve = alt.Chart(filtered_fit_df).mark_line(
        ).encode(
            x=alt.X(
                "Checkpoint Step:Q",
                sort=None,
                axis=alt.Axis(labels=True),
                scale=alt.Scale(domain=x_domain)
            ),
            y=alt.Y(
                "Accuracy (normalized):Q",
                axis=alt.Axis(labels=False),
                scale=alt.Scale(domain=y_domain)
            ),
            color=alt.Color(
                "Language:N", 
                sort=None,
                scale=alt.Scale(scheme="category20")
            ),
        ).properties(
            width=width,
            height=height        
        ).interactive()
        
        points = alt.Chart(filtered_df).mark_point(
        ).encode(
            x=alt.X(
                "N",
                axis=alt.Axis(labels=True),
                scale=alt.Scale(domain=x_domain)
            ),
            y=alt.Y(
                "Accuracy (normalized):Q",
                scale=alt.Scale(domain=y_domain)
            ),
            color=alt.Color(
                "Language:N", 
                scale=alt.Scale(scheme="category20")
            ),
            tooltip=[
                "Language:N",
                "Task:N",
                "Accuracy",
                "Accuracy (normalized):Q",
                "Step:Q",
                "Tokens:N",
                
            ],
        ).properties(
            width=width,
            height=height        
        ).interactive()
            
        chart = (curve + points).properties(
            title=task
        )
        charts.append(chart)
    
    return charts