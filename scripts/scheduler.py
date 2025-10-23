# scripts/scheduler.py
import schedule
import time
import asyncio
import logging
from src.main import TikTokIncrementalScraper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ScraperScheduler:
    def __init__(self):
        self.scraper = TikTokIncrementalScraper()
        self.setup_schedule()
    
    def setup_schedule(self):
        # Schedule every 6 hours
        schedule.every(6).hours.do(self.run_scraping_job)
        logger.info("Scheduler setup: running every 6 hours")
    
    async def scrape_all_profiles(self):
        """Get profiles from database and scrape them"""
        # In practice, read from config or database
        profiles = ["tiktok", "example_user"]  # Replace with your profiles
        return await self.scraper.scrape_profiles(profiles)
    
    def run_scraping_job(self):
        """Wrapper for scheduling"""
        logger.info("Starting scheduled scraping job")
        try:
            asyncio.run(self.scrape_all_profiles())
            logger.info("Scheduled scraping job completed")
        except Exception as e:
            logger.error(f"Scheduled job failed: {e}")
    
    def run(self):
        """Main scheduler loop"""
        logger.info("Scraper scheduler started")
        # Run immediately on startup
        self.run_scraping_job()
        
        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    scheduler = ScraperScheduler()
    scheduler.run()
