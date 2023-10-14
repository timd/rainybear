import { NextApiRequest, NextApiResponse } from 'next';
import AWS from 'aws-sdk';
import { createObjectCsvStringifier } from 'csv-writer';

// Initialize AWS SDK
AWS.config.update({
  accessKeyId: process.env.AWS_ACCESS_KEY_ID,
  secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
  region: 'us-west-1', // or your AWS region
});

const s3 = new AWS.S3();

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    const { description, title, author, url } = req.body;

    // Create CSV content from JSON data
    const csvStringifier = createObjectCsvStringifier({
      header: [
        { id: 'description', title: 'DESCRIPTION' },
        { id: 'title', title: 'TITLE' },
        { id: 'author', title: 'AUTHOR' },
        { id: 'url', title: 'URL' },
      ],
    });

    const records = [
      { description, title, author, url },
    ];

    const csvContent = csvStringifier.stringifyRecords(records);

    // Prepare data for S3 upload
    const uploadParams = {
      Bucket: 'Your-S3-Bucket-Name',
      Key: `your-folder/${title}.csv`, // File name you want to save as
      Body: csvContent,
      ContentType: 'text/csv',
    };

    // Upload CSV file to S3
    s3.upload(uploadParams, (err, data) => {
      if (err) {
        res.status(500).json({ error: 'Error uploading to S3' });
        return;
      }
      res.status(200).json({ success: true, message: 'Successfully uploaded to S3', data });
    });
  } else {
    res.status(405).json({ error: 'Method not allowed' });
  }
}
