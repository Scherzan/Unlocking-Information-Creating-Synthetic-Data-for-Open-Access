from pyecharts import options as opts
from pyecharts.charts import Tree

data = [
    {
        "children": [
            {
                "children": [
                    {
                        "children": [
                            {"name": "Statistical Moments \n" "and Tests"},
                            {"name": "Distance Calculations"},
                            {"name": "Visual Comparisons"},
                        ],
                        "name": "Univariate",
                    },
                    {
                        "children": [
                            {"name": "Pairwise Pearson \n" "Correlation"},
                            {"name": "Contingency Table"},
                        ],
                        "name": "Multivariate",
                    },
                    {
                        "children": [
                            {"name": "PCA Plots Comparison"},
                            {"name": "Isomap Plots Comparison"},
                        ],
                        "name": "Dimensional",
                    },
                    {
                        "children": [
                            {
                                "name": "Train classifier to label\n"
                                "real and synthetic records\n"
                                "and analyse its performance"
                            },
                        ],
                        "name": "Data Labeling",
                    },
                ],
                "name": "Resemblance Analysis",
            },
            {
                "children": [
                    {
                        "children": [
                            {
                                "name": """Choose a prediction
                                            task within your data, \n
                                            train your prediction model
                                            on real data, \n"
                                            "train your prediction model
                                            on synthetic data, \n"
                                            "compare prediction task
                                            performance on real test data \n"""
                            }
                        ],
                        "name": """"Downstream Task
                                           Evaluation""",
                    }
                ],
                "name": "Utility Evaluation",
            },
            {
                "children": [
                    {
                        "children": [
                            {"name": "Paired Euclidean Distance"},
                            {"name": "Wasserstein distance"},
                            {"name": "Jensen-Shannon divergence"},
                        ],
                        "name": "Similarity Evaluation Analysis (SEA)",
                    },
                    {
                        "children": [
                            {"name": "Membership Inference Attack"},
                            {"name": "Attribute Inference Attack"},
                        ],
                        "name": "Re-Identification Risk Analysis (RIRA)",
                    },
                ],
                "name": "Privacy Evaluation",
            },
            {
                "children": [
                    {
                        "children": [
                            {"name": "Basic Statistical Properties"},
                            {"name": "Correlation Matrices"},
                            {"name": "PCA"},
                            {"name": "Utility Evaluation (ML-Task)"},
                        ],
                        "name": "Similarity Score \n" "(Brenninkmeijer & Hille)",
                    },
                    {
                        "children": [
                            {"name": "Basic Statistical Properties"},
                            {"name": "Correlation Score"},
                            {"name": "Utility Evaluation (ML-Task)"},
                            {"name": "Propensity Mean Squared Error"},
                            {"name": "Support Coverage"},
                        ],
                        "name": "TabSynDex \n" "(Chundawat et al.)",
                    },
                    {
                        "children": [
                            {
                                "name": """Resemblance Analysis
                                   (URA, MRA, DRA, DLA)"""
                            },
                            {
                                "name": """Utility Evaluation
                                   (classification)"""
                            },
                            {"name": "Privacy Evaluation (SEA, RIRA)"},
                        ],
                        "name": "Categorization of Quality \n" "(Hernandez et al.)",
                    },
                    {
                        "children": [
                            {"name": "Univariate Statistical \n" "Tests"},
                            {"name": "Correlation and \n" "Contingency Measures"},
                        ],
                        "name": "Quality Score \n" "(Synthetic Data Vault)",
                    },
                ],
                "name": "One Overall Metric",
            },
        ],
        "name": "Evaluation Metrics",
    }
]
c = Tree().add(
    "",
    data,
    label_opts=opts.LabelOpts(font_size=18, position="top", color="#1f449c"),
    initial_tree_depth=0,
    itemstyle_opts=opts.ItemStyleOpts(border_color0="000000"),
)
