# backlink_generator_features_v2.py

class BacklinkGeneratorFeatures:
    def __init__(self):
        self.features = {
            "Automated Outreach": "Automates the process of contacting webmasters for backlinks.",
            "Campaign Tracking": "Tracks the progress of multiple link-building campaigns.",
            "Analytics Integration": "Integrates with Google Analytics for backlink performance tracking.",
            "Bulk Backlink Submission": "Allows for bulk submission of backlinks to directories and platforms.",
            "Link Quality Analysis": "Analyzes the quality of backlinks and flags spammy links.",
            "Link Reporting": "Provides detailed reports on the backlinks acquired.",
            "SEO Dashboard": "A centralized dashboard to monitor all SEO campaigns.",
            "Data Export": "Exports data in multiple formats such as CSV and Excel.",
            "Proxy Integration": "Supports proxy integration for safer outreach.",
            "User Management": "Manages multiple users for team collaboration."
        }

    def display_features(self):
        print("Backlink Generator Software Features:")
        for feature, description in self.features.items():
            print(f"{feature}: {description}")

    def get_feature(self, feature_name):
        return self.features.get(feature_name, "Feature not found.")

# Example usage:
if __name__ == "__main__":
    bg_features = BacklinkGeneratorFeatures()
    bg_features.display_features()
    # To get details for a specific feature:
    print(bg_features.get_feature("SEO Dashboard"))
